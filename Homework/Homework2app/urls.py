from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client', views.client, name='client'),
    path('about', views.about, name='about'),
    path('index', views.index, name='index'),
    path('create_client', views.create_client, name='create_client')
]
