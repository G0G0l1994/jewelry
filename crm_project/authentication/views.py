from django.shortcuts import render,redirect

from .forms import CustomUserCreateForm
from .models import User

# Create your views here.

def registration(request):

    if request.method == 'POST':


        form = CustomUserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('/login/')
        # else:
        #     # return redirect('/registrations/')
        #     return render(request, 'crm_project/registration.html', {'form': form})

    else:
        form = CustomUserCreateForm()
        
    return render(request, 'crm_project/registration.html', {'form':form})



