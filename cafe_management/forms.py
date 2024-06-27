from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'sugar', 'Coffee','Flour','Chocolate','milk','vertical','price','image'] 
