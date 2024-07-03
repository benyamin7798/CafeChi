from django import forms
from main.models import Product,Warehouse

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'sugar', 'Coffee','Flour','Chocolate','milk','vertical','price','image'] 

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['sugar', 'coffee', 'flour', 'chocolate', 'milk']

