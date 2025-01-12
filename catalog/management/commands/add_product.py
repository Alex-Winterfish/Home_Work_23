# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add product to the database'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(category_name='Кондитерские изделия')

        products = [
            {'product_name': 'Ириска', 'product_description': 'Вязкая конфета, для удаления зубных пломб',
             'product_image': '/images/butterscotch.jpg','product_price': 54, 'category_name': category},
            {'product_name': 'Вафли', 'product_description': 'Хрустящая сладость', 'product_price': 43,
             'category_name': category},
            {'product_name': 'Леденцы', 'product_description': 'Долгоиграющая конфета из патоки',
             'product_price': 54, 'category_name': category}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.product_name}'))

        category, _ = Category.objects.get_or_create(category_name='Молочные продукты')

        products = [
            {'product_name': 'Творог', 'product_description': 'Кисломолочный продукт',
             'product_price': 54, 'category_name': category},
            {'product_name': 'Сметна 15%', 'product_description': 'Кисломолочный продукт 15% жирности', 'product_price': 43,
             'category_name': category},
            {'product_name': 'Молоко', 'product_description': 'Коровье молоко 5% жирности', 'product_price': 54,
             'category_name': category}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.product_name}'))

        category, _ = Category.objects.get_or_create(category_name='Мясные продукты')

        products = [
            {'product_name': 'Докторская колбаса', 'product_description': 'Вареная колбаса из отходов '
                                                                          'мясного производства',
             'product_price': 54, 'category_name': category},
            {'product_name': 'Московская', 'product_description': 'Сырокопченая колбаса из отходов мясного'
                                                                  ' производства', 'product_price': 43,
             'category_name': category},
            {'product_name': 'Нарезка индилайт', 'product_description': 'Мясной продукт из бедер индейки',
             'product_price': 54,
             'category_name': category}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.product_name}'))