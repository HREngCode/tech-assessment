from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_id', 'order_date', 'product_number']
        depth = 1

    customer_id = serializers.IntegerField(write_only=True)