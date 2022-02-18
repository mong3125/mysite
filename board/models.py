from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    WEATHER = {('sunny', '맑음'), ('cloudy', '구름'), ('rainy', '비'), ('snow', '눈'), ('storm', '폭풍'), ('destroy', '멸망')}

    subject = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    feelingWeather = models.CharField(max_length=10, choices=WEATHER, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)