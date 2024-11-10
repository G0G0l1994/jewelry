from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'contact_number']

class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'contact_number']
    