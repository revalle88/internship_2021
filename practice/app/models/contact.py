from django.contrib.auth import get_user_model

from django.db import models

from django.conf import settings

User = get_user_model()


class Contact(models.Model):
    class Type:
        SALE_MANAGER = 'sale'
        PURCHASE_MANAGER = 'purchase'
        ALL = (
            (SALE_MANAGER, 'Продажи'),
            (PURCHASE_MANAGER, 'Закупки'),
        )

    type = models.CharField(max_length=200, choices=Type.ALL)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    value = models.CharField(max_length=200)