# Generated by Django 2.1.7 on 2019-04-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_post_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='service',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]