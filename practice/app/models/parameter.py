from django.db import models


class Parameter(models.Model):
    name = models.CharField(max_length=200)
