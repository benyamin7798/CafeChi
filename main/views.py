from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product

class HomePageView(TemplateView):
    model = Product
    template_name = 'base.html'