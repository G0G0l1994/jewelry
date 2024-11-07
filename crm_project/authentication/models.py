from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    role = models.CharField(max_length=50,blank = True, default='3d')
    contact_number = models.CharField(max_length=30,blank = True, null =True)

    REQUIRED_FIELDS = ['first_name', 'last_name','role']
    USERNAME_FIELD = 'username'

    def __repr__(self):

        return f"{self.first_name} {self.last_name} {self.role}"
    

# Create your models here.
