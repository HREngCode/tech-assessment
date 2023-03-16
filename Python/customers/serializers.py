from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'age', 'address', 'address_id', 'phone_number']
        depth = 1

    address_id = serializers.IntegerField(write_only=True)