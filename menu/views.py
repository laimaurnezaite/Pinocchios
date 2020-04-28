from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


# Create your views here.

class MenuListView(ListView):
    model = Product
    template_name = 'main_list.html'

class MenuItemDetailView(DetailView):
    model = Product
    template_name = 'menu_item_detail.html'


