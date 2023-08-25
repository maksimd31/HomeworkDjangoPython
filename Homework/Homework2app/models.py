from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)  # буквы
    email = models.EmailField()
    telefone_number = models.IntegerField()
    adress = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    product_name = models.CharField(max_length=150)
    product_descripsion = models.TextField(blank=True)
    product_price = models.IntegerField()
    product_quantiti = models.IntegerField(max_length=100)
    product_add_date = models.DateTimeField(auto_now=True)
    product_photo = models.ImageField(upload_to='photos/%y/%m%d/')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    total_price = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
