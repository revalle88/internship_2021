from practice.app.models.product import Product

from django.db import models


class ProductInfo(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    price_rrc = models.DecimalField(decimal_places=2, max_digits=12)
