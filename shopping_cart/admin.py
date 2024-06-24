from django.contrib import admin
from .models import PurchaseHistory,Order

@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['user','product','purchase_date']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','created_at','completed']





