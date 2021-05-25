from django.urls import path

from app.views import import_products

urlpatterns = [
    path('import_products/', import_products, name='import'),
]
