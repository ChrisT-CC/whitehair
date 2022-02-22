""" Models file """
from django.db import models
from django.contrib.auth.models import User


class Proverb(models.Model):
    """Proverbs Django model"""
    content = models.CharField(max_length=200, unique=True)
    meaning = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.content
