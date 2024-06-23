from django.urls import path
from . import views

urlpatterns = [
    # path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('', views.cart_detail, name='cart_detail'),

    
    path('summary/', views.order_summary, name='order_summary'),
    path('finalize/', views.finalize_order, name='finalize_order'),
    path('success/', views.order_success, name='order_success'),

]