from django.urls import path

from .views import MenuListView, MenuItemDetailView


urlpatterns = [
    path('<int:pk>/', MenuItemDetailView.as_view(), name='item_detail'),
    # path('<int:pk>/add', AddToOrder(), name='add'),
    path('', MenuListView.as_view(), name='main_list'),
]