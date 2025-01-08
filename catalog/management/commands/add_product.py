# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add product to the database'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(category_name='Кондитерские изделия')

        products = [
            {'product_name': 'Ириска', 'product_description': 'Вязкая конфета, для удаления зубных пломб', 'product_price': 54, 'category_name': category},
            {'product_name': 'Вафли', 'product_description': 'Хрустящая сладость', 'product_price': 43, 'category_name': category},
            {'product_name': 'Леденцы', 'product_description': 'Долгоиграющая конфета из патоки', 'product_price': 54, 'category_name': category}
        ]



        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.product_name}'))

