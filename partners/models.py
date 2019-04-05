from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLS by reversing the URL patterns
from django.contrib.auth.models import User  # Required to assign User as a Partner
from datetime import date
from ckeditor.fields import RichTextField
#from team.models import Team


class Partner(models.Model):
    delegate = models.ForeignKey(User, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=True, blank=True)
    ministry_name = models.CharField(max_length=200, blank=True, null=True)
    ministry_location = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, help_text='e.g partner role, organisation, ministry' )
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)
    membership_date = models.DateTimeField(default=datetime.now, blank=True, null=True, help_text='Date when partner joined')
    def __str__(self):
        return self.ministry_name