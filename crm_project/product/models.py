from django.db import models
from customer.models import Customer


TYPE_CHOICE = [('повеска','подвеска'), 
               ('кольцо','кольцо'),
               ('брошь','брошь'), 
               ('серьги','серьги'), 
               ('комплект', 'комплект'),
               ('пусеты', 'пусеты'), 
               ('другое', 'другое'),
               ('колье','колье'),
               ('браслет','браслет')
               ]



class Product(models.Model):

    name = models.CharField(max_length=100, blank = True)
    type_product = models.CharField(max_length=30,choices=TYPE_CHOICE,blank=True,default='кольцо')
    customer = models.ForeignKey(Customer,related_name='customer', on_delete=models.CASCADE)
    price = models.IntegerField()
    create_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(auto_created=False)
    expiration_date = models.DateField(auto_created=False)
    comment = models.TextField()
    
# Create your models here.
