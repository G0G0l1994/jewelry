from django.shortcuts import render,redirect

from django.contrib.auth import logout

def home(request):
    
    return render(request,'crm_project/main.html')


def about(request):

    return render(request, 'crm_project/about.html')

def logout_user(request):

    logout(request)

    return redirect('home')
