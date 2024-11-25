from django.db import models

from customer.models import Customer
from authentication.models import User


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
STATUS_CHOICE = (('1','принят'),
    ("2","в работе"),
    ("4","правки"),
    ("3","согласование"),
    ("5", "на росте"),
    ("6","выполнен")
)
    


class Product(models.Model):

    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='product',on_delete=models.CASCADE,null=True)
    on_work = models.BooleanField(default=False,null=True)
    worker = models.ForeignKey(User,related_name='worker',null=True,on_delete=models.CASCADE)
    work_time = models.TextField(max_length=200,default='00 дней 00 часов 00 минут', null=True)
    type_product = models.CharField(max_length=30,choices=TYPE_CHOICE,default='кольцо')
    customer = models.ForeignKey(Customer,related_name='customer', on_delete=models.CASCADE)
    price = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_created=False, null=True)
    expiration_date = models.DateField(auto_created=False)
    comment = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,null=True,default='1')

    
    def __str__(self):
        return f'{self.name} {self.start_date} {self.status}'
