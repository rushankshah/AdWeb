import math
import random
from adtool.models import AdvertisementClient


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
                advertisement_html = self.advertisement_html_maker(
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
        random_pk = self.model.objects.count()*random.random()
        random_pk = math.floor(random_pk) + 1
        random_advertisement = self.model.objects.get(pk=random_pk)
        return random_advertisement

    def advertisement_html_maker(self, advertisement):
        advertisement_site = f"http://{self.request.get_host()}/site/api/advertisement/{advertisement.pk}"
        advertisement_image = f"http://{self.request.get_host()}{advertisement.ad_image.url}"
        advertisement_html = f"<a href=\"{advertisement_site}\"><img src=\"{advertisement_image}\"></a>"
        return advertisement_html

    def key_confirmation(self, user_key):
        if AdvertisementClient.objects.get(userKey=user_key):
            return True
        else:
            return False
