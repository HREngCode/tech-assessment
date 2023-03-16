from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Address
        fields = ['id', 'street_address', 'city', 'state', 'postal_code']
        # depth = 1

