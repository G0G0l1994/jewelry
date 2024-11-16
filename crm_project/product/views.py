from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from datetime import datetime

from .forms import AddProductForm
from .models import Product

@login_required
def add_product(request):

    if request.method == 'POST':

        form = AddProductForm(request.POST)
        print(request.POST)

        if form.is_valid():
            
            product = form.save()
            product.save()
            
            return redirect('dashboard/product')
    else:    
        
        form = AddProductForm()

    return render(request, 'product/add_product.html', {
        'form': form
        })

@login_required
def product_list(request):

    products = Product.objects.all()

    return render(request,'product/product_list.html', {'products': products})


@login_required
def product_detail(request, pk):
    
    product = Product.objects.get(pk=pk)

    form = AddProductForm()

    if request.method == 'POST':
        date = datetime.now()
        product.start_date = date.today()
        
        product.save()

    return render(request, 'product/product_detail.html', {'product':product,
                                                           'form': form})


    