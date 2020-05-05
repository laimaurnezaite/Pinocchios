from django.urls import path

from .views import menu_list, menu_item 

urlpatterns = [
    path('', menu_list, name='main_list'),
    path('<int:pk>/', menu_item, name='item_detail'),

]