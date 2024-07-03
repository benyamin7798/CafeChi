# views.py
from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
<<<<<<< HEAD
from .models import Product
from shopping_cart.models import Order
=======
from .models import Product,Warehouse
from shopping_cart.models import Order,OrderItem
>>>>>>> Ben
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from shopping_cart.models import Product ,PurchaseHistory
from collections import defaultdict
from datetime import datetime


# class HomePageView(TemplateView):
#     template_name = 'homepage.html'

def home(request):
    top_products = Product.objects.order_by('-sales_count')[:6]
    return render(request, 'homepage.html', {'top_products': top_products})

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


def product_list_view(request, vertical):
    products = Product.objects.filter(vertical=vertical)
<<<<<<< HEAD
    return render(request, 'product_list.html', {'products': products, 'vertical': vertical})


    


=======
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user, completed=False).first()
        order_items = OrderItem.objects.filter(order=order) if order else []
        print(f'prder items: {order_items}')
        product_quantities = {item.product.id: {'quantity': item.quantity, 'price': item.product.price} for item in order_items}

        return render(request, 'product_list.html', {
            'products': products,
            'vertical': vertical,
            'product_quantities': product_quantities
    })
    else:
        return redirect('login')
>>>>>>> Ben

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

def product_list(request):
    products = Product.objects.all()  # fetch all products from the database
    return render(request, 'product_list.html', {'products': products})
