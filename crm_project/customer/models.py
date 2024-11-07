from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=200, blank = True)
    phone_number = models.CharField(max_length=30, blank = True)
    comment = models.TextField()


    def __str__(self):
        return f"{self.name} {self.phone_number}"
    

