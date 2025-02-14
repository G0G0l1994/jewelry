from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

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

class LoginView(LoginView):
    redirect_authenticated_user = True 

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request,*args,**kwargs)


def home(request):
    
    return render(request,'crm_project/main.html')


def about(request):

    return render(request, 'crm_project/about.html')

def logout_user(request):

    logout(request)

    return redirect('home')




