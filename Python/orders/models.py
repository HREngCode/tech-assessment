from django.db import models
from customers.models import Customer

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    product_number = models.CharField(max_length=30)