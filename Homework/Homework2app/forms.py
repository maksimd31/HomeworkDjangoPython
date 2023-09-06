from django import forms
from .models import Products


class ClientForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_description', 'product_price', 'product_quantity', 'product_photo']
