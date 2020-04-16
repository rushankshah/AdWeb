from django.contrib import admin
from .models import Advertisement, AdvertisementClient, AdvertisementLog
# Register your models here.

admin.site.register(Advertisement)
admin.site.register(AdvertisementClient)
admin.site.register(AdvertisementLog)
