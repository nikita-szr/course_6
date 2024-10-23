from .models import Product, Category
from django.core.cache import cache


class ProductService:

    @staticmethod
    def get_products_by_category(category_id):
        cache_key = f'products_category_{category_id}'

        products = cache.get(cache_key)
        if not products:

            products = Product.objects.filter(category_id=category_id)

            cache.set(cache_key, products, timeout=60 * 15)

        return products

    @staticmethod
    def get_category_name(category_id):
        category = Category.objects.get(id=category_id)
        return category.name
