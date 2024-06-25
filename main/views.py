# views.py
from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from .models import Product
from shopping_cart.models import Order
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from shopping_cart.models import Product ,PurchaseHistory
from collections import defaultdict
from datetime import datetime


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

def alaki(request):
    return render(request,'alaki.html')

def management(request):
    return render(request,'management.html')



# def purchase_history(request):
#     user = request.user
#     purchases = PurchaseHistory.objects.filter(user=user).order_by('-purchase_date')

#     grouped_purchases = defaultdict(list)
#     for purchase in purchases:
#         grouped_purchases[purchase.purchase_date.date()].append(purchase)
    
#     return render(request, 'purchase_history.html', {'grouped_purchases': dict(grouped_purchases), 'user': user})
@login_required
def purchase_history(request):
    user = request.user
    orders = Order.objects.filter(user=user, completed=True).order_by('-created_at')

    return render(request, 'purchase_history.html', {'orders': orders, 'user': user})