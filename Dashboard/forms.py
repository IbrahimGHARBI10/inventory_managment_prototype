from django import forms
from .models import order, product

class ProductForm(forms.ModelForm):
    class Meta:
        model=product
        fields= ['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model= order
        fields= ['product','order_quantity']
