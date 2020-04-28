from django.urls import path

from . import views
# from .views import OrderDetail, AddToOrderView, AddToOrder
# from .views import OrderDetail, AddToOrderView 
from .views import OrderDetail, AddToOrder , confirmOrder

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    # path('add/', AddToOrderView.as_view(), name='add'),
    path('add/', AddToOrder, name='add'),
    path('confirm/', confirmOrder, name='confirm'),
]
