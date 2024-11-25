from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from product.models import Product



@login_required
def dashboard(request):

    products = Product.objects.filter(on_work = True)


    return render(request, 'dashboard/dashboard.html', {'products': products})
# Create your views here.
