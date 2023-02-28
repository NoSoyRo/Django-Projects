from django.db import models

# Create your models here.

class Customer(models.Model):
    store_id = models.IntegerField(blank=False)
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    email = models.CharField(max_length=200,blank=False)
    address_id = models.CharField(max_length=200,blank=False)
    active = models.IntegerField(blank=False)
    create_date = models.CharField(max_length=2000,blank=False)
    last_update = models.CharField(max_length=2000,blank=False)