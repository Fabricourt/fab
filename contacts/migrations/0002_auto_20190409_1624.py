# Generated by Django 2.1.7 on 2019-04-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='post_education_level',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='post_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='post_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
