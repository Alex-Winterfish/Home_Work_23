from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.


def product_info(request):
    product = Product.objects.get(id=25)
    context = {
        'product_name': product.product_name,
        'product_description': product.product_description,
        'product_price': product.product_price,
    }
    return render(request, 'product_info.html', context)