from django.shortcuts import render,redirect

from .forms import CustomerForms

def add_customer(request):

    if request.method == 'POST':

        form = CustomerForms(request.POST)

        if form.is_valid():

            customer = form.save()
            customer.save()

            return redirect('dashboard')
    else:

        form = CustomerForms()

    return render(request, 'customer/add_customer.html', {'form':form})    


# Create your views here.
