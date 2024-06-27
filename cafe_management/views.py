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


def dashbord(request):
    return render(request,'dashbord.html')



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