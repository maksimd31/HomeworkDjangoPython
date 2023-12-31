# Generated by Django 4.2.4 on 2023-08-23 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone_number', models.IntegerField()),
                ('adress', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('product_descripsion', models.TextField(blank=True)),
                ('product_price', models.IntegerField()),
                ('product_quantiti', models.IntegerField(max_length=100)),
                ('product_add_date', models.DateTimeField(auto_now=True)),
                ('product_photo', models.ImageField(upload_to='photos/%y/%m%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homework2app.client')),
                ('products', models.ManyToManyField(to='Homework2app.products')),
            ],
        ),
    ]
