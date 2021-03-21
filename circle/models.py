from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

User = settings.AUTH_USER_MODEL

ALCOHOL_LIST = ((0, '少なめもしくは無'),(1, 'どちらかといえば少なめ'),(2, '普通'),(3, 'どちらかといえば多め'),(4, '多め'))
HARD_LIST = ((0, '緩め'),(1, 'どちらかといえば緩め'),(2, '普通'),(3, 'どちらかというとまじめ'),(4, 'まじめ'))
GENDER_RATE = ((0, '0%'),(1, '10%'),(2, '20%'),(3, '30%'),(4, '40%'),(50, '50%'),(6, '60%'),(7, '70%'),(8, '80%'),(9, '90%'),(10, '100%'))
EXPERIENCED_LIST = ((0, '20%以下'),(1, '20% ～ 40%'),(2, '40% ～ 60%'),(3, '60% ～ 80%'),(4, '80%以上'))
EVENT_LIST = ((0, '少なめもしくは無'),(1, 'どちらかといえば少なめ'),(2, '普通'),(3, 'どちらかといえば多め'),(4, '多め'))

class Circle(models.Model):
    class Meta:
        verbose_name = 'サークルデータ'
        verbose_name_plural = 'サークルデータ'

    owner = models.ForeignKey(User, verbose_name='代表者', default=1, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(verbose_name='スラッグ', unique=True)
    image = models.ImageField(verbose_name='サークル画像', upload_to='media/image/', blank=True, null=True)
    name =  models.CharField(verbose_name='サークル名', max_length=100)
    description = models.TextField(verbose_name='アピールポイント', null=True, blank=True, max_length=400)
    budget = models.PositiveIntegerField(verbose_name='年会費', null=True, blank=True)
    members_num = models.PositiveIntegerField(verbose_name='人数', null=True, blank=True)
    gender_rate = models.IntegerField(verbose_name='男女比率', choices=GENDER_RATE, null=True, blank=True)
    alcohol = models.IntegerField(verbose_name='飲み会頻度', choices=ALCOHOL_LIST, default=3)
    hard = models.IntegerField(verbose_name='練習雰囲気', choices=HARD_LIST, null=True, blank=True, default=3)
    experienced = models.IntegerField(verbose_name="テニス経験者率", choices=EXPERIENCED_LIST, null=True, blank=True)
    event = models.IntegerField(verbose_name="イベント頻度", choices=EVENT_LIST, null=True, blank=True)
    practice_date = models.CharField(verbose_name='活動日',max_length=20, default='', null=True, blank=True)
    practice_place = models.CharField(verbose_name='活動場所',max_length=20, default='', null=True, blank=True)
    twitter_url = models.URLField(verbose_name='Twitter',null=True, blank=True)
    insta_url = models.URLField(verbose_name='Instagram', null=True, blank=True)
    line_url = models.URLField(verbose_name='Line', null=True, blank=True)
    liked = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        return self.name

    def num_likes(self):
        return self.liked.all().count()
        
    class Meta:
        ordering = ['id']

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.circle}-{self.value}"