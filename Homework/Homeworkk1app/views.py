import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

# logger = logging.getLogger('homework1')
logger = logging.getLogger('homework1')


# Create your views here.
def home(reqwest):
    """
    Главная
    :param reqwest:
    :return:
    """
    # return HttpResponse('HM_DJ_PY/Homework1/html/home.html')

    return render(reqwest, 'home.html')


def about_me(reqwest):
    """
    О бо мне
    :param reqwest:
    :return:
    """
    return render(reqwest, 'about.html')


def index(reqwest):
    return render(reqwest, 'home.html')


def index2(reqwest):
    """
    Пример использования исключения 404
    :param reqwest:
    :return:
    """
    if reqwest > 2:
        raise Http404
    return render(reqwest, 'home.html')


def index3(reqwest):
    """
    Пример использования редирект перенаправление страницы
    :param reqwest:
    :return:
    """
    if reqwest > 2:
        return redirect('home')  # перебрасывает на главную страницу код 302 Временно поменял код
        # return redirect('/',permanent=True) # постоянно поменянный код 301
    return render(reqwest, 'home.html')


def pageNotFound(reqwest, exception):
    """
    Обработчик финишной страницы исключения 404
    :param reqwest:
    :param exception:
    :return:
    """
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
