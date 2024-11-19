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
STATUS_CHOICE = (('принят','принят'),
    ("в работе","в работе"),
    ("правки","правки"),
    ("согласование","согласование"),
    ("на росте", "на росте"),
    ("выполнен","выполнен")
)
    


class Product(models.Model):

    name = models.CharField(max_length=100)
    type_product = models.CharField(max_length=30,choices=TYPE_CHOICE,default='кольцо')
    customer = models.ForeignKey(Customer,related_name='customer', on_delete=models.CASCADE)
    price = models.IntegerField()
    create_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(auto_created=False, null=True)
    expiration_date = models.DateField(auto_created=False)
    comment = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,null=True)

    
    def __str__(self):
        return f'{self.name} {self.start_date} {self.status}'
