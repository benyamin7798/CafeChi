from django.urls import path
from .views import (HomePageView,
                    product_list_view,
<<<<<<< HEAD
                    alaki,
                    management,
=======
>>>>>>> sajad_backend
                    purchase_history)
from shopping_cart.views import checkout


urlpatterns = [
    path('',HomePageView.as_view(),name='homepage'),
    path('products/<str:vertical>/', product_list_view, name='product_list'),
    path('checkout/', checkout, name='checkout'),
<<<<<<< HEAD
    path('alaki/',alaki,name='alaki'),
    path('management/',management,name='management'),
=======
>>>>>>> sajad_backend
    path('purchase-history/', purchase_history, name='purchase_history'),
    
]
