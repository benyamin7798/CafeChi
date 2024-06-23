# views.py
from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from .models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class HomePageView(TemplateView):
    template_name = 'homepage.html'

# class ProductListView(ListView):
#     model = Product
#     template_name = 'product_list.html'
#     context_object_name = 'products'

#     def get_queryset(self):
#         vertical = self.kwargs.get('vertical')
#         return Product.objects.filter(vertical=vertical)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['vertical'] = self.kwargs.get('vertical')
#         return context

# views.py

def product_list_view(request, vertical):
    products = Product.objects.filter(vertical=vertical)
    return render(request, 'product_list.html', {'products': products, 'vertical': vertical})


