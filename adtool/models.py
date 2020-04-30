from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import hashlib
from .custom_mixin import ModelDiffMixin
# Create your models here.




class Advertisement(ModelDiffMixin, models.Model):
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
    
    def save(self, force_insert=False, force_update=False):
        if self.has_changed:
            if 'clicks' in self.changed_fields:
                AdvertisementLog.objects.create(ad=self)
        super(Advertisement, self).save(force_insert, force_update)

class AdvertisementLog(models.Model):
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    click_date = models.DateTimeField('date clicked', default=timezone.now)


# These are people who display advertisements


class AdvertisementClient(models.Model):
    userKey = models.TextField(
        max_length=32, default='00000000000000000000000000000000')

    def __str__(self):
        return self.userKey

    # Generate an md5 hash key
    def save(self, *args, **kwargs):
        self.userKey = str(hashlib.md5(str(self.userKey).encode()).hexdigest())
        super(AdvertisementClient, self).save(*args, **kwargs)
