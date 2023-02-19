from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    price = models.IntegerField()


class Order(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)


class ItemsToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    item_quantity = models.IntegerField(default=1)
