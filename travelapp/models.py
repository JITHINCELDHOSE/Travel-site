import datetime

from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField()

    def __str__(self):
        return self.name


class destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    cities = models.IntegerField()

    def __str__(self):
        return self.name



