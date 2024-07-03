from django.urls import path
from .views import (dashbord,
                    add_product,
                    product_list,
                    edit_product,
                    delete_product,
                    edit_warehouse,)
                    


urlpatterns = [
    path('dashbord/',dashbord,name='dashbord'),
    path('add_product/',add_product,name='add_product'),
    path('products/', product_list, name='product_list'),
    path('products/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('edit_warehouse/',edit_warehouse,name='edit_warehouse'),
]
