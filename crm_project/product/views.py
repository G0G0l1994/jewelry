from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddProductForm

@login_required
def add_product(request):

    if request.method == 'POST':

        form = AddProductForm(request.POST)
        print(request.POST)

        if form.is_valid():
            
            product = form.save()
            product.save()
            return redirect('dashboard')
    else:    
        
        form = AddProductForm()

    return render(request, 'crm_project/add_product.html', {
        'form': form
        })