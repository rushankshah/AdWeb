# Generated by Django 3.0.4 on 2020-03-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adtool', '0002_auto_20200324_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='genre',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
