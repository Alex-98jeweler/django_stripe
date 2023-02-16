from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    price = models.IntegerField()