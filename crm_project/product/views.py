from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import localtime

from datetime import datetime, timezone


from .forms import AddProductForm
from .models import Product
from .service import stop_work

@login_required
def add_product(request):

    if request.method == 'POST':
        
        form = AddProductForm(request.POST)
        

        if form.is_valid():
            
            product = form.save()
            product.created_by = request.user
            product.save()

            messages.success(request, 'Изделие добавлено')
            
            return redirect('product_list')
    else:    
        
        form = AddProductForm()

    return render(request, 'product/add_product.html', {
        'form': form
        })

@login_required
def product_list(request):

    products = Product.objects.all().order_by('expiration_date')

    return render(request,'product/product_list.html', {'products': products})


@login_required
def product_detail(request, pk):
    
    product = Product.objects.get(pk=pk)

    form = AddProductForm()

    if request.method == 'POST':
        
        product.start_date = localtime()
        
        product.on_work = True
        product.status = '2'

        
        product.save()

    return render(request, 'product/product_detail.html', {'product':product,
                                                           'form': form})


@login_required
def product_update(request,pk):
    
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)
    

    if request.method == 'POST':

        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            
            form.save()
            
            messages.success(request, 'Изделие изменено')

            return redirect('product_list')
        else:
            form = AddProductForm(instance=product)
            print(form.data)

        return render(request, 'product/product_update.html', {
                'form': form
                })


@login_required
def product_delete(request,pk):

    product = get_object_or_404(Product,pk=pk)
    product.delete()

    messages.success(request, 'Изделие удалено')
    return redirect('product_list')

@login_required
def update_time(request,pk):
    query = get_object_or_404(Product,pk=pk)
    

    if request.method == 'POST':
        local = localtime()
        work = stop_work(query, localtime=local)
        
        query.on_work = False
        query.work_time= work
        query.start_date = local
        query.save()


        return redirect('product_detail',pk)






    