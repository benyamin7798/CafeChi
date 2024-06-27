from django.urls import path
from .views import (dashbord,
                    add_product)


urlpatterns = [
    path('dashbord/',dashbord,name='dashbord'),
    path('add_product/',add_product,name='add_product'),
]
