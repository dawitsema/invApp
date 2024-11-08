from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'sku', 'price', 'quantity', 'suplier']
        labels  = {
            'product_id' : 'Product ID',
            'name' : 'Name',
            'sku' : 'SKU',
            'price' : 'Price',
            'quantity' : 'Quantity',
            'suplier' : 'Suplier',
        }
        
        widgets = {
            'product_id' : forms.NumberInput(attrs={'placeholder': 'e.g. 1','class':'form-control'}),
            'name' : forms.TextInput(attrs={'placeholder': 'e.g. Apple','class':'form-control'}),
            'sku' : forms.TextInput(attrs={'placeholder': 'e.g. S123456','class':'form-control'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'e.g. 1.00','class':'form-control'}),
            'quantity' : forms.NumberInput(attrs={'placeholder': 'e.g. 1','class':'form-control'}),
            'suplier' : forms.TextInput(attrs={'placeholder': 'e.g. Apple Inc.','class':'form-control'}),
        }
    