# Generated by Django 3.0.4 on 2020-05-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addisplay', '0003_auto_20200511_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='userkey',
            field=models.CharField(default='0', max_length=32),
        ),
    ]
