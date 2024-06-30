from django import forms
from django.core.exceptions import ValidationError
from .models import Warehouse

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def clean(self):
        if Warehouse.objects.exists() and not self.instance.pk:
            raise ValidationError('فقط یک انبار میتواند ساخته شود')
        return super().clean()


