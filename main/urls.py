from django.urls import path
from .views import (home,
                    product_list_view,
                    purchase_history)
from shopping_cart.views import checkout


urlpatterns = [
    path('',home,name='homepage'),
    path('products/<str:vertical>/', product_list_view, name='product_list'),
    path('checkout/', checkout, name='checkout'),
    path('purchase-history/', purchase_history, name='purchase_history'),
    
]
