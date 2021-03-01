from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Circle(models.Model):
    owner = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='media/image/', blank=True, null=True)
    name =  models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=400)
    twitter_url = models.URLField(null=True, blank=True)
    insta_url = models.URLField(null=True, blank=True)
