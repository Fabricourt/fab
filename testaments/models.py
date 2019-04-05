from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
#from partners.models import Partner

class Testament(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ministry_name = models.CharField(max_length=200, null=True, blank=True)
    message = RichTextField(max_length=999, blank=True, null=True)
    post_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} {self.ministry_name}'
    
    def save(self, **kwargs):
        super().save()
