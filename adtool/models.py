from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import hashlib
from .custom_mixin import ModelDiffMixin
from addisplay.models import Website
# Create your models here.




class Advertisement(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    url_link = models.URLField(default="")
    clicks = models.IntegerField(default=0)
    category = models.CharField(max_length=30, default="")
    size = models.CharField(
            max_length=16, choices=(
            ('medium rectangle', '300x250 pixels'),
            ('large rectangle', '336x280 pixels'),
            ('leaderboard', '728x90 pixels'),
            ('half page', '320x600 pixels'),
            ('free size', 'free size')
        ), 
        default='free size')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class AdvertisementLog(models.Model):
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    site = models.ForeignKey(Website, on_delete=models.PROTECT)
    click_date = models.DateTimeField('date clicked', default=timezone.now)

