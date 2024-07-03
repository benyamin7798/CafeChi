<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect , get_object_or_404
from .forms import ProductForm,WarehouseForm
from main.models import Product,Warehouse
from shopping_cart.models import PurchaseHistory
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum
import json
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta
from django.db.models import Sum
from shopping_cart.models import OrderItem


def dashbord(request):
    is_admin = request.user.is_authenticated and request.user.is_staff
    today = datetime.today()
    date_filter = request.GET.get('date_filter', 'weekly')
    product_id = request.GET.get('product', None)  # دریافت ID محصول

    if date_filter == 'monthly':
        start_date = today - timedelta(days=30)
    else:  # پیش فرض: هفتگی
        start_date = today - timedelta(days=7)

    sales_data = []
    product_name = ''

    if product_id:
        sales_data = (OrderItem.objects
                      .filter(order__created_at__range=[start_date, today], product_id=product_id)
                      .values('order__created_at__date')
                      .annotate(total_sales=Sum('quantity'))
                      .order_by('order__created_at__date'))
        
        product_name = Product.objects.get(id=product_id).name  # نام محصول را دریافت کنید

    dates = [sale['order__created_at__date'].strftime('%Y-%m-%d') for sale in sales_data]
    sales = [sale['total_sales'] for sale in sales_data]
    products = Product.objects.all()  # دریافت لیست محصولات

    return render(request, 'dashbord.html', {
        'dates': dates,
        'sales': sales,
        'products': products,
        'selected_product': product_id,
        'product_name': product_name,
        'date_filter': date_filter,
        'is_admin': is_admin
    })



def add_product(request):
    message = ""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            message = f'Product "{product.name}" was successfully created.'
            if 'add_and_continue' in request.POST:
                return render(request, 'add_product.html', {'form': ProductForm(), 'message': message})
            elif 'add_and_view' in request.POST:
                return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form, 'message': message})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'admin_product.html', {'products': products})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            if 'add_and_continue' in request.POST:
                message = f'Product "{product.name}" was successfully updated.'
                return render(request, 'add_product.html', {'form': ProductForm(), 'message': message})
            #messages.success(request, f'Product "{product.name}" was successfully updated.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_list.html')


def edit_warehouse(request):
    warehouse = get_object_or_404(Warehouse, id=1)  # فرض می‌کنیم id انبار همیشه 1 است
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Warehouse was successfully updated.')
            return redirect('dashbord')
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'edit_warehouse.html', {'form': form})

def sales_data(request):
    pass


# def sales_chart_view(request):
#     today = datetime.today()
#     date_filter = request.GET.get('date_filter', 'weekly')
#     product_id = request.GET.get('product', None)  # دریافت ID محصول

#     if date_filter == 'monthly':
#         start_date = today - timedelta(days=30)
#     else:  # پیش فرض: هفتگی
#         start_date = today - timedelta(days=7)

#     sales_data = []
#     product_name = ''

#     if product_id:
#         sales_data = (OrderItem.objects
#                       .filter(order__created_at__range=[start_date, today], product_id=product_id)
#                       .values('order__created_at__date')
#                       .annotate(total_sales=Sum('quantity'))
#                       .order_by('order__created_at__date'))
        
#         product_name = Product.objects.get(id=product_id).name  # نام محصول را دریافت کنید

#     dates = [sale['order__created_at__date'].strftime('%Y-%m-%d') for sale in sales_data]
#     sales = [sale['total_sales'] for sale in sales_data]
#     products = Product.objects.all()  # دریافت لیست محصولات

#     return render(request, 'dashbord.html', {
#         'dates': dates,
#         'sales': sales,
#         'products': products,
#         'selected_product': product_id,
#         'product_name': product_name,
#         'date_filter': date_filter
#     })
>>>>>>> sajad_backend
