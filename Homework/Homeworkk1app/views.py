import logging

from django.shortcuts import render
from django.http import HttpResponse

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
    return render(reqwest, 'about_me.html')


def index(reqwest):
    return render(reqwest, 'home.html')
