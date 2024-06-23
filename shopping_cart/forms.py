from django import forms
from main.models import Product

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1,max_value=12,initial=1)


    def clean_product_id(self):
        product_id = self.cleaned_data.get('product_id')

        if not Product.objects.filter(id=product_id).exists():
            raise forms.ValidationError('Invalid product ID')
        return product_id
    
    