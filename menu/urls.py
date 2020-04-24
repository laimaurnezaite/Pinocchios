from django.urls import path

from .views import MainListView, ToppingsListView, FreeToppingsView

urlpatterns = [
    path('main/', MainListView.as_view(), name='main_list'),
    path('toppings/', ToppingsListView.as_view(), name='toppings_list'),
    path('toppingsforpizza/', FreeToppingsView.as_view(), name = 'pizza_toppings_list'),

]