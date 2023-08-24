from django.shortcuts import render

from Homework2app.models import Client

# Create your views here.

menu = ['О  сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(reqwest):
    return render(reqwest, 'Homework2/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(reqwest):
    return render(reqwest, 'Homework2/about.html', {'title': 'О сайте'})


def client(reqwest):
    posts = Client.objects.all() # выводим все данные из таблицы клиенты
    return render(reqwest, 'Homework2/client.html', {'posts': posts, 'title': 'Все клиенты'})
