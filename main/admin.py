from .forms import WarehouseForm
from django.contrib import admin
from .models import Product,Warehouse

@ admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'vertical')

@admin.register(Warehouse)
class WareHouseAdmin(admin.ModelAdmin):
    form = WarehouseForm
    list_display = ('sugar','coffee','flour','chocolate','milk')
