from django.urls import path

from .views import MenuListView, MenuItemDetailView


urlpatterns = [
    path('', MenuListView.as_view(), name='main_list'),
    path('menu/<int:pk>/', MenuItemDetailView.as_view(), name='item_detail'),
]