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
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from django.contrib.admin.views.decorators import staff_member_required
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.http import HttpResponse


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

@login_required
@staff_member_required
def sales_dashboard(request):
    product_id = request.GET.get('product')
    products = Product.objects.all()
    
    if product_id:
        product = Product.objects.get(id=product_id)
        # فیلتر کردن خریدها بر اساس تاریخ و محصول
        sales_data = PurchaseHistory.objects.filter(
            product=product,
            purchase_date__gte=timezone.now() - datetime.timedelta(days=30)
        ).values('purchase_date').annotate(total_sales=models.Sum('quantity'))

        # آماده‌سازی داده‌ها برای نمودار
        dates = [data['purchase_date'].date() for data in sales_data]
        sales = [data['total_sales'] for data in sales_data]

        # ایجاد نمودار
        fig, ax = plt.subplots()
        ax.bar(dates, sales, color='blue')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total Sales')
        ax.set_title(f'Sales Data for {product.name}')
        fig.autofmt_xdate()

        # ذخیره نمودار به یک فایل درون حافظه
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close(fig)

        # ارسال نمودار به کاربر
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'inline; filename="sales_chart.png"'
        response.write(buffer.getvalue())
        return response
    else:
        return render(request, 'sales_dashboard.html', {'products': products})
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

