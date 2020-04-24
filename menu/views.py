from django.shortcuts import render
from django.views.generic import ListView

from .models import MainDish, FreeToppings, Toppings

# Create your views here.

class MainListView(ListView):
    model = MainDish
    template_name = 'main_list.html'

class ToppingsListView(ListView):
    model = Toppings
    template_name = 'toppings_list.html'

class FreeToppingsView(ListView):
    model = FreeToppings
    template_name = 'pizza_toppings_list.html'