from django.urls import path
from . import views

urlpatterns = [

    path('summary/', views.order_summary, name='order_summary'),
    path('finalize/', views.finalize_order, name='finalize_order'),
    path('checkout/', views.checkout, name='checkout'),
    
]