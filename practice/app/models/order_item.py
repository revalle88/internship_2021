from django.db import models

from practice.app.models.order import Order
from practice.app.models.product import Product
from practice.app.models.shop import Shop


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
