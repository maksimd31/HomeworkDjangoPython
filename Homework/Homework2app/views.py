from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Products, Order

# Create your views here.

menu = ['О  сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(reqwest):
    return render(reqwest, 'Homework2/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(reqwest):
    return render(reqwest, 'Homework2/about.html', {'title': 'О сайте'})


def client(reqwest):
    posts = Client.objects.all()  # выводим все данные из таблицы клиенты
    return render(reqwest, 'Homework2/client/client.html', {'posts': posts, 'title': 'Все клиенты'})


def product(reqwest):
    all_product = Products.objects.all()
    return render(reqwest, 'Homework2/client/client.html', {'posts': all_product, 'title': 'Все Продукты'})


def create_client(request):
    """
    Функция добавления нового клиента
    :param request:
    :return:
    """
    try:
        if request.method == 'POST':
            client_name = request.POST.get('client_name')
            client_email = request.POST.get('client_email')
            client_telefone_number = request.POST.get('client_telefone_number')
            client_adress = request.POST.get('client_adress')
            new_client = Client(name=client_name, email=client_email, telefone_number=client_telefone_number,
                                adress=client_adress)
            new_client.save()
            # return HttpResponse('Клиент успешно создан')
            return render(request, 'Homework2/client/client_add.html')
        else:
            return render(request, 'Homework2/client/create_client.html')
    except Exception as e:
        print(f"При создании клиента4 возникло исключение: {e}")
        return render(request, 'Homework2/client/client_exeption.html')


def read_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'read_client.html', {'client': client})


def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.name = request.POST.get('client_name')
        client.email = request.POST.get('client_email')
        client.telefone_number = request.POST.get('client_telefone_number')
        client.adress = request.POST.get('client_adress')
        client.save()
        return HttpResponse('Данные обновлены')
    else:
        return render(request, 'update_client.html', {'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return HttpResponse('Клиент удален')


def create_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_descripsion = request.POST.get('product_descripsion')
        product_price = request.POST.get('product_price')
        product_quantiti = request.POST.get('product_quantiti')
        product_photo = request.FILES['product_photo']
        new_product = Products(product_name=product_name, product_descripsion=product_descripsion,
                               product_price=product_price, product_quantiti=product_quantiti,
                               product_photo=product_photo)
        new_product.save()
        return HttpResponse('Продукт добавлен в базу')
    else:
        return render(request, 'create_product.html')


def read_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'read_product.html', {'product': product})


def update_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.product_descripsion = request.POST.get('product_descripsion')
        product.product_price = request.POST.get('product_price')
        product.product_quantiti = request.POST.get('product_quantiti')
        product.product_photo = request.FILES['product_photo']
        product.save()
        return HttpResponse('Редактирование прошло успешно')
    else:
        return render(request, 'update_product.html', {'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    return HttpResponse('Продукт удален')


def create_order(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        products_id = request.POST.getlist('product_id')
        total_price = request.POST.get('total_price')
        new_order = Order(client_id=client_id, total_price=total_price)
        new_order.save()
        for product_id in products_id:
            product = get_object_or_404(Products, id=product_id)
            new_order.products.add(product)
        return HttpResponse('Заказ создан успешно')
    else:
        clients = Client.objects.all()
        products = Products.objects.all()
        return render(request, 'create_order.html', {'clients': clients, 'products': products})


def read_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'read_order.html', {'order': order})


def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        products_id = request.POST.getlist('product_id')
        total_price = request.POST.get('total_price')
        order.client_id = client_id
        order.total_price = total_price
        order.products.clear()
        for product_id in products_id:
            product = get_object_or_404(Products, id=product_id)
            order.products.add(product)
        order.save()
        return HttpResponse('Заказ успешно обновлен')
    else:
        clients = Client.objects.all()
        products = Products.objects.all()
        return render(request, 'update_order.html', {'order': order, 'clients': clients, 'products': products})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return HttpResponse('Заказ успешно удален')
