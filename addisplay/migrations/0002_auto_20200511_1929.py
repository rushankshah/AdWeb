# Generated by Django 3.0.4 on 2020-05-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addisplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='userkey',
            field=models.TextField(max_length=32),
        ),
    ]
