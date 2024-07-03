
# views.py
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem,PurchaseHistory
from main.models import Warehouse






@login_required
def checkout(request):
    if request.method == 'POST':
        cart_data = request.POST.get('cart', '')
        try:
            cart = json.loads(cart_data)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'})

        if not cart:
            return JsonResponse({'success': False, 'error': 'Empty cart'})

        order, created = Order.objects.get_or_create(user=request.user, completed=False)
        for product_id, details in cart.items():
            product = Product.objects.get(id=product_id)
            order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)
            order_item.quantity = details['quantity']
            order_item.save()

        order.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})








@login_required
def order_summary(request):
    try:
        order = Order.objects.get(user=request.user, completed=False)
    except Order.DoesNotExist:
        order = None
    print(f'order: {order}')
    if order:
        order_items = order.items.all()
        total_price = sum(item.product.price * item.quantity for item in order_items)
    else:
        order_items = None
        total_price = 0

    context = {
        'order_items': order_items,
        'total_price': total_price
    }

    return render(request, 'order_summary.html', context)




@login_required
def finalize_order(request):
    if request.method == 'POST':
        order = Order.objects.filter(user=request.user, completed=False).first()
        if order:
            order.completed = True
            order.save()

            # ثبت سفارشات در PurchaseHistory و به‌روزرسانی فروش محصول
            for item in order.items.all():
                #total_price = item.quantity * item.product.price
                
                PurchaseHistory.objects.create(
                    user=request.user,
                    product=item.product,
                    quantity=item.quantity,
                    total_price=item.quantity * item.product.price
                )

                # به‌روزرسانی تعداد فروش محصول
                product = item.product
                product.sales_count += item.quantity
                product.save()

            return redirect('homepage')
    return redirect('homepage')