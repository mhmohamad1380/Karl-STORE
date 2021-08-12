from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopList.as_view()),
    path('sidebar', views.sidebar,name='sidebar'),
    path('<str:title>/<int:id>', views.productDetail),
]
