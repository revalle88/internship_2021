from django.http import HttpResponse
from django.shortcuts import render
import sys, os
import yaml

import practice
from app.models import Shop, Category, Product, ProductInfo


# Create your views here.
def import_products(request):
    ProductInfo.objects.all().delete()
    Product.objects.all().delete()
    Category.objects.all().delete()
    Shop.objects.all().delete()

    dir = os.path.dirname(practice.__file__)
    file_path = os.path.join(dir, 'shop1.yaml')
    print(file_path)

    with open(file_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        shop_dict = yaml.load(file, Loader=yaml.FullLoader)
        print(shop_dict)

        shop = shop_dict['shop']
        shop_model = Shop(name=shop)
        shop_model.save()
        for category in shop_dict['categories']:
            category_model = Category(id=category['id'], name=category['name'])
            category_model.save()
            category_model.shops.add(shop_model)
            category_model.save()

        for good in shop_dict['goods']:
            product = Product(
                id=good['id'],
                category_id=good['category'],
                name=good['name'],
            )
            product.save()
            product_info = ProductInfo(
                product=product,
                price=good['price'],
                price_rrc=good['price_rrc'],
                shop=shop_model,
                quantity=good['quantity']
            )
            product_info.save()




    return HttpResponse("You're looking at question OK")