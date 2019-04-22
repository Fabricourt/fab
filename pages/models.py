from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image




class Post(models.Model):
    profession = models.CharField(max_length=100)
    service = models.CharField(max_length=200, blank=True, null=True)
    why_you_essay = RichTextField(blank=True, null=True)
    resume = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    education_level = models.CharField(max_length=100, null=True, blank=True)
    expirience = models.CharField(max_length=100, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    home = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=200, null=True, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_fulltime = models.BooleanField()
    is_parttime = models.BooleanField()
    is_employee = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    
    def __str__(self):
        return self.profession

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



