from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),\
    #
    path('', views.index, name='home'),
    path('/client', views.client, name='client')
]
