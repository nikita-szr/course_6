from .models import Product, Category


class ProductService:

    @staticmethod
    def get_products_by_category(category_id):

        return Product.objects.filter(category_id=category_id)

    @staticmethod
    def get_category_name(category_id):
        category = Category.objects.get(id=category_id)
        return category.name
