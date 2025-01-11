from django import forms


from .models import Product
from authentication.models import User

class AddProductForm(forms.ModelForm):
    

    class Meta:
        model = Product
        fields = ("name",
                  "type_product",
                  "customer",
                  "price",
                  "expiration_date",
                  "comment",
                  "status",
                  "worker"
                  )
    def __init__(self,*args,**kwargs):
        super(AddProductForm,self).__init__(*args,**kwargs)
        self.fields['worker'].queryset = User.objects.filter(role='3d')
