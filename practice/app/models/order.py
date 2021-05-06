from django.utils import timezone
from django.contrib.auth import get_user_model

from django.db import models

from django.conf import settings

User = get_user_model()


class Order(models.Model):
    status = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(default=timezone.now, verbose_name='время создания заказа')

