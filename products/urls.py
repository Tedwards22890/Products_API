from django.urls import path
from . import views

urlpattern = [
    path('', views.products_list),
]