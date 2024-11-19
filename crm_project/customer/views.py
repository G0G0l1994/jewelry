from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomerForms
from .models import Customer



@login_required
def customer_add(request):

    if request.method == 'POST':

        form = CustomerForms(request.POST)

        if form.is_valid():

            customer = form.save()
            customer.save()

            return redirect('customer_list')
    else:

        form = CustomerForms()

    return render(request, 'customer/customer_add.html', {'form':form})    

@login_required
def customer_list(request):

    customers = Customer.objects.all()

    return render(request, 'customer/customer_list.html',{'customers':customers})


@login_required
def customer_detail(request,pk):

    customer = get_object_or_404(Customer,pk=pk)

    return render(request, 'customer/customer_detail.html', {
        'customer': customer
        })


@login_required
def customer_update(request,pk):

    customer = get_object_or_404(Customer,pk=pk)
    print(customer)
    if request.method == 'POST':
        
        form = CustomerForms(request.POST,instance=customer)
        print('post')
        if form.is_valid():
            print('post')
            form.save()
        
            messages.success(request, 'Данные заказчика обновлены')

            return redirect('customer_list')
        
        else:

            form = CustomerForms(instance=customer)
            print('get')
    return render(request,'customer/customer_update.html', {
            'form': form
            })

@login_required
def customer_delete(request, pk):

    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()

    messages.success(request, 'Данные заказчика удалены')

    return redirect('customer_list')