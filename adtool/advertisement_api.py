import math
import os
from django.conf import settings
from random import randint
import base64
import os.path
from adtool.models import AdvertisementClient
from PIL import Image
from django.db.models.aggregates import Count

class AdvertisementAPI:

    def __init__(self, request, advertisement_model):
        super().__init__()
        self.model = advertisement_model
        self.request = request

    def get_advertisement(self, user_key, type="SLEEPING"):
        # Gives back an html string of the advertisement or error
        try:
            if self.key_confirmation(user_key):
                advertisement = self.advertisement_selection()
                # Retrieve advertisement image from Database here and send it as json
                advertisement_html = self.advertisement_html_maker_base64(
                    advertisement)
                return advertisement_html
            else:
                # If key_confirmation is false we raise an exception
                raise Exception()
        except ValueError as e:
            raise e

    def advertisement_selection(self):
        # Decides how are advertisements retrieved from database
        # it is in random mode
        count=self.model.objects.aggregate(count=Count('id'))['count']
        random_index=randint(0, count-1)
        return self.model.objects.all()[random_index] 

    def advertisement_html_maker(self, advertisement):
        advertisement_site = f"http://{self.request.get_host()}/site/api/advertisement/{advertisement.pk}"
        advertisement_image = f"http://{self.request.get_host()}{advertisement.image.url}"
        advertisement_html = f"<a href=\"{advertisement_site}\"><img src=\"{advertisement_image}\"></a>"
        return advertisement_html

    def advertisement_html_maker_base64(self, advertisement):
        img_path = advertisement.image.path
        image = Image.open(img_path)
        img_format = image.format.lower()
        with open(img_path, 'rb') as f:
            img = base64.b64encode(f.read()).decode('utf-8')
        advertisement_site = f"http://{self.request.get_host()}/site/api/advertisement/{advertisement.pk}"
        advertisement_image = f"<img src=\"data:images/{img_format};base64,{img}\">"
        advertisement_html = f"<a href=\"{advertisement_site}\"><img src=\"data:images/{img_format};base64,{img}\"></a>"
        return advertisement_html

    def key_confirmation(self, user_key):
        if AdvertisementClient.objects.get(userKey=user_key):
            return True
        else:
            return False
