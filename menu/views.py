from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

# Create your views here.

class MenuListView(ListView):
    model = Product
    template_name = 'main_list.html'