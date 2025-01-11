from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from product.models import Product
from customer.models import Customer



@login_required
def dashboard(request):

    products = Product.objects.all()
    

    customers = Customer.objects.all()

    if request.user.role == '3d':

        products = Product.objects.filter(worker_id = request.user.id)
        return render(request, 'dashboard/dashboard-3d.html', {'products': products,
                                                        })
    else:
        
        return render(request, 'dashboard/dashboard-manager.html', {'products': products,
                                                        'customers': customers})

# Create your views here.
