from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200, help_text="Enter field documentation")

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'

    def __str__(self):
        return str(self.name)
