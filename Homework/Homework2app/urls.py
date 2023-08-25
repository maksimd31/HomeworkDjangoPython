from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client', views.client, name='client'),
    path('about', views.about, name='about'),
    path('index', views.index, name='index'),
    path('create_client', views.create_client, name='create_client'),
    path('read_client', views.read_client, name='read_client'),
    path('read_client_form', views.read_client, name='read_client_form')
]
