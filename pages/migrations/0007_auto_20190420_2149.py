# Generated by Django 2.1.7 on 2019-04-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_post_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]