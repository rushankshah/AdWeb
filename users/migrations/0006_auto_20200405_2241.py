# Generated by Django 3.0.4 on 2020-04-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200405_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='', max_length=256),
        ),
    ]
