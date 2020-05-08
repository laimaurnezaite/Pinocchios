from django.urls import path

from .views import home, menu_item 

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', menu_item, name='item_detail'),

]