from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


# Create your views here.


def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product_name': product.product_name,
        'product_description': product.product_description,
        'product_price': product.product_price,
    }
    return render(request, 'product_info.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)



def add_product(request):
    if request.method == "POST":
        name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        price = request.POST.get('product_price')
        prod_category = request.POST.get('category_name')
        category = Category.objects.get(category_name=prod_category)
        product = Product.objects.create(product_name=name, product_description=description,
                                         product_price=price, category_name=category)

    return render(request, 'add_product.html')

def contacts(request):
    return render(request, 'contacts.html')