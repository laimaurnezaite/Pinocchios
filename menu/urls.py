from django.urls import path

# from .views import MenuListView, MenuItemDetailView, menu_list
from .views import menu_list, MenuItemDetailView



urlpatterns = [
    path('<int:pk>/', MenuItemDetailView.as_view(), name='item_detail'),
    # path('', MenuListView.as_view(), name='main_list'),
    path('', menu_list, name='main_list'),

]