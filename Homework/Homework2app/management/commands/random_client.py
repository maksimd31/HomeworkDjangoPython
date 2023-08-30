import random
from faker import Faker
from django.core.management.base import BaseCommand
from Homework2app.models import Client


class Command(BaseCommand):
    help = 'Fill Client table with random data'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        for i in range(100):
            name = fake.name()
            email = fake.email()
            telefone_number = random.randint(1000000000, 9999999999)
            adress = fake.address()
            date = fake.date_this_century()

            client = Client(name=name, email=email, telefone_number=telefone_number,
                            adress=adress, date=date)
            client.save()
        self.stdout.write(self.style.SUCCESS('Успешно заполненная таблица клиенты со случайными данными'))
