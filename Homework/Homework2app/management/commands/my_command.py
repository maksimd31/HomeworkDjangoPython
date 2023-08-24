from django.core.management.base import BaseCommand
from Homework2app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Ivanov Vasilii',email='ivanovvast@mail.ru',telefone_number='11111111',adress='parshina l1 l1')
        client.save()
        self.stdout.write(f'{client}')


