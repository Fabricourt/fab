# Generated by Django 2.1.7 on 2019-04-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20190421_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
