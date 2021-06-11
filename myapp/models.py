from django.db import models

# Create your models here.
class MyModel(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    