from django.urls import path

from . import views
# from .views import OrderDetail, AddToOrderView, AddToOrder
# from .views import OrderDetail, AddToOrderView 
from .views import OrderDetail, confirmOrder, confirmed_orders, shopping_cart

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('add/', shopping_cart, name='add_to_cart'),
    path('confirm/', confirmOrder, name='confirm'),
    path('confirmed/', confirmed_orders, name='confirmed_orders'),
]
