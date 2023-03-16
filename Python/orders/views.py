from django.shortcuts import render
from rest_framework import status
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Order
from .serializers import OrderSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_orders(request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([AllowAny]) 
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny]) 
def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)