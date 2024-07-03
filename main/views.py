# views.py
from django.shortcuts import render,redirect
from .models import Product,Warehouse
from shopping_cart.models import Order,OrderItem
from django.contrib.auth.decorators import login_required
from shopping_cart.models import Product 




def home(request):
    top_products = Product.objects.order_by('-sales_count')[:6]
    return render(request, 'homepage.html', {'top_products': top_products})




def product_list_view(request, vertical):
    products = Product.objects.filter(vertical=vertical)
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user, completed=False).first()
        order_items = OrderItem.objects.filter(order=order ) if order else []
        product_quantities = [{'quantity': item.quantity, 'price': item.product.price,'id':item.product.id} for item in order_items]
        warehouse = Warehouse.objects.first()

        return render(request, 'product_list.html', {
            'products': products,
            'vertical': vertical,
            'product_quantities': product_quantities,
            'warehouse': warehouse,
    })
    else:
        return redirect('login')


@login_required
def purchase_history(request):
    user = request.user
    orders = Order.objects.filter(user=user, completed=True).order_by('-created_at')

    return render(request, 'purchase_history.html', {'orders': orders, 'user': user})


