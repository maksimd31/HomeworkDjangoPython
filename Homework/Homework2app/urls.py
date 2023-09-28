from django.urls import path
from . import views
from .views import product_list, product_detail, add_product
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('client', views.client, name='client'),
    path('about', views.about, name='about'),
    path('index', views.index, name='index'),
    path('create_client', views.create_client, name='create_client'),
    path('read_client', views.read_client, name='read_client'),
    path('read_client_form', views.read_client, name='read_client_form'),
    path('report', views.orders_in_past_days, name='report'),
    path('product_list', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('testJs', views.testJs, name='testJs'),

]
