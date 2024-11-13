from django import forms

from .models import Product


class AddProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("name",
                  "type_product",
                  "customer",
                  "price",
                  "expiration_date",
                  "comment",
                  "status")

