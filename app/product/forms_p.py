from django import forms
from product.models import Product


class Product_form_for_create(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name_product',
            'description',
            'price',
            'image',
        )
