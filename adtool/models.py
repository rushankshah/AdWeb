from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import hashlib
# Create your models here.


CATEGORY_CHOICES = (
    ('sleeping', 'SLEEPING'),
    ('banner', 'BANNER'),
    ('popup', 'POPUP'),
)


class Advertisement(models.Model):
    name = models.CharField(max_length=50)
    ad_image = models.ImageField(upload_to='images/')
    url_link = models.URLField(default="")
    clicks = models.IntegerField(default=0)
    genre = models.CharField(max_length=30, default="")
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default='sleeping')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

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
