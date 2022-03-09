from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    content = models.TextField()
    is_complete = models.BooleanField(default=False)
