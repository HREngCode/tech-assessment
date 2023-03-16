from rest_framework import serializers
from .models import Address


class CustomerAddressSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Address
        fields = ['id', 'street_address', 'city', 'state', 'postal_code']
        depth = 1

