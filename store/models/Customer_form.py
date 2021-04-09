from django.db import  models
from django.core.validators import MinLengthValidator
from .customer import Customer
import datetime



class Contact1(models.Model):
    Relation = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    dob = models.DateField(default=datetime.datetime.today)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
