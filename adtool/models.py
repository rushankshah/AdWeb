from django.db import models

# Create your models here.


class Advertisement(models.Model):
    name = models.CharField(max_length=50)
    ad_image = models.ImageField(upload_to='images/')
    clicks = models.IntegerField(default=0)
    #genre = models.CharField(max_length=30, default=None)
    category = models.CharField(max_length=10, default='sleeping')

    def __str__(self):
        return self.name
