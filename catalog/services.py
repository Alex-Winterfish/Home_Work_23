from .models import Product

class ProductService:

    @staticmethod
    def get_category_product(category_id):
        products = Product.objects.filter(category_name=category_id)
        if not products.exists():
            return None
        else:
            return products