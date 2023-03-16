from django.db import models

# Create your models here.
class Address(models.Model):
    street_address = models.CharField( max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)