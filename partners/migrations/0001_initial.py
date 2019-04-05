# Generated by Django 2.1.7 on 2019-04-05 05:55

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ministry_location', models.CharField(blank=True, max_length=100, null=True)),
                ('county', models.CharField(blank=True, max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='e.g partner role, organisation, ministry')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('is_published', models.BooleanField(default=False)),
                ('membership_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when partner joined', null=True)),
                ('delegate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]