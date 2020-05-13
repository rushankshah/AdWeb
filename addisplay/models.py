from django.db import models
from django.contrib.auth.models import User
import string
import secrets


class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    userkey = models.CharField(max_length=32, default='0')


    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        notfound = True
        while notfound:
            key = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(32))
            if not Website.objects.filter(userkey=key).exists():
                notfound = False
                self.userkey = key
        super(Website, self).save(*args, **kwargs)
        