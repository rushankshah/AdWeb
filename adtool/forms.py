from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ['name', 'ad_image', 'url_link', 'genre', 'category']
