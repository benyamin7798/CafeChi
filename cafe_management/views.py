from django.shortcuts import render

def dashbord(request):
    return render(request,'dashbord.html')

from django.shortcuts import render, redirect
from .forms import ProductForm

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
                return redirect('alaki')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form, 'message': message})
