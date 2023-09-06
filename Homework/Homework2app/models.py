from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)  # буквы
    email = models.EmailField()
    telefone_number = models.IntegerField()
    adress = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'

    def __repr__(self):
        return f'{self.name} {self.email}'


class Products(models.Model):
    product_name = models.CharField(max_length=150)
    product_description = models.TextField(blank=True)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_add_date = models.DateTimeField(auto_now=True)
    product_photo = models.ImageField(upload_to='photos/%y/%m%d/')

    def __str__(self):
        return f'{self.product_name}'

    def __repr__(self):
        return f'{self.product_name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    total_price = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}'

    def __repr__(self):
        return f'{self.client}'


'''
# Запись в бд через shell django интерфейс orm
# python manage.py shell
# >>> from Homework2app.models import Client импортируем models
# >>> Client.objects.create(name='Ivanov Vasilii',email='ivanovvast@mail.ru',
# telefone_number='11111111',adress='parshina l1 l1')
# таким образом можно сразу добавлять в базу клиентов
так же есть еще запросы
create(), all(), filter(), exclude(), get()
'''

'''
Вывод сех объектов из бд 
>>> Client.objects.all()
<QuerySet [<Client: Client object (1)>, <Client: Client object (2)>]>
'''


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


def __repr__(self):
    return self.name
