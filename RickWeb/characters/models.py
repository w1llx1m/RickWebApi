from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField(max_length=150)