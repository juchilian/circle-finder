from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Circle(models.Model):
    owner = models.ForeignKey(User, verbose_name='代表者', default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(verbose_name='サークル画像', upload_to='media/image/', blank=True, null=True)
    name =  models.CharField(verbose_name='サークル名', max_length=100)
    description = models.TextField(verbose_name='概要', null=True, blank=True, max_length=400)
    twitter_url = models.URLField(verbose_name='Twitter',null=True, blank=True)
    insta_url = models.URLField(verbose_name='Instagram', null=True, blank=True)

    def __str__(self):
        return self.name
    