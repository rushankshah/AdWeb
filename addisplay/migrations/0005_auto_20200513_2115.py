# Generated by Django 3.0.4 on 2020-05-13 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addisplay', '0004_auto_20200511_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='client',
        ),
        migrations.AddField(
            model_name='website',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
