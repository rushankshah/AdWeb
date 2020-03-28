from django import forms
from .models import Advertisement

# Redundant


class AdvertisementForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AdvertisementForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(AdvertisementForm, self).save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Advertisement
        fields = ['name', 'ad_image', 'url_link', 'genre', 'category']
