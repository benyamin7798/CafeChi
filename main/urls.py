from django.urls import path
from .views import (HomePageView,
                    product_list_view)

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',HomePageView.as_view(),name='homepage'),
    path('products/<str:vertical>/', product_list_view, name='product_list'),
    
]
