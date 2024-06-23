from django.urls import path
from .views import (HomePageView,
                    product_list_view,
                    alaki)
from shopping_cart.views import checkout

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',HomePageView.as_view(),name='homepage'),
    path('products/<str:vertical>/', product_list_view, name='product_list'),
    path('checkout/', checkout, name='checkout'),
    path('alaki/',alaki,name='alaki')
    
]
