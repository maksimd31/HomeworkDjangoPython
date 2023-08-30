import random
from django.core.management.base import BaseCommand
from Homework2app.models import Client, Products, Order


class Command(BaseCommand):
    help = 'Fill Order table with random data'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Products.objects.all()
        for i in range(100):
            client = random.choice(clients)
            order = Order(client=client, total_price=0)
            order.save()
            for j in range(random.randint(1, 10)):
                product = random.choice(products)
                order.products.add(product)
                order.total_price += product.product_price
            order.save()
        self.stdout.write(self.style.SUCCESS('Успешно заполненная таблица заказов со случайными данными'))
