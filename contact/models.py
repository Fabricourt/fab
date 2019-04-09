from django.db import models
from datetime import datetime

class Contact(models.Model):
  post = models.CharField(max_length=200, blank=True, null=True )
  post_id = models.IntegerField()
  name = models.CharField(max_length=200, blank=True, null=True )
  email = models.CharField(max_length=400, blank=True, null=True )
  phone = models.CharField(max_length=100, blank=True, null=True )
  message = models.TextField(blank=True, null=True )
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True, null=True )
  def __str__(self):
    return self.name