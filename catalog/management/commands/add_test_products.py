from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Удаляет все продукты и категории, затем добавляет тестовые продукты'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING('Все продукты и категории были удалены.'))

        electronics = Category.objects.create(name='Электроника', description='Гаджеты и техника')
        books = Category.objects.create(name='Книги', description='Книги')

        self.stdout.write(self.style.SUCCESS(f'Созданы категории: {electronics.name}, {books.name}'))

        Product.objects.create(
            name='Ноутбук',
            description='Для офиса',
            price=100000,
            category=electronics
        )
        Product.objects.create(
            name='Смартфон',
            description='Устройства связи',
            price=800,
            category=electronics
        )
        Product.objects.create(
            name='Питон для новичков',
            description='Обучение питону',
            price=2000,
            category=books
        )

        self.stdout.write(self.style.SUCCESS('Добавлены тестовые продукты.'))
