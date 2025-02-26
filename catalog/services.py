from .models import Product
from django.core.cache import cache

class ProductService:

    @staticmethod
    def get_category_product(category_id):
        products = cache.get(f'products_in_category_{category_id}')
        if not products:
            products = Product.objects.filter(category_name=category_id)
            cache.set(f'products_in_category_{category_id}', products, 60 * 15)
            if not products.exists():
                return None
            else:
                return products
        return products
