import random
from faker import Faker
from django.core.management.base import BaseCommand
from Homework2app.models import Products


class Command(BaseCommand):
    help = 'Fill Products table with random data'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        for i in range(100):
            product_name = fake.word()
            product_descripsion = fake.text()
            product_price = random.randint(1, 1000)
            product_quantiti = random.randint(1, 100)
            product_photo = None

            product = Products(product_name=product_name, product_descripsion=product_descripsion,
                               product_price=product_price, product_quantiti=product_quantiti,
                               product_photo=product_photo)
            product.save()
        self.stdout.write(self.style.SUCCESS('Успешно заполненная таблица продукты со случайными данными'))
