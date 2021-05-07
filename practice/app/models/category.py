from django.db import models

from app.models.shop import Shop


class Category(models.Model):
    shops = models.ManyToManyField(Shop, blank=True, related_name="categories", verbose_name="Категория")
    name = models.CharField(max_length=200)
