from django.urls import path

from . import views
from .views import confirmOrder, confirmed_orders, shopping_cart, add

urlpatterns = [
    path('add/', add, name='add_to_cart'),
    path('shopping_cart', shopping_cart, name='shopping_cart'),
    path('confirm/', confirmOrder, name='confirm'),
    path('confirmed/', confirmed_orders, name='confirmed_orders'),
]
