from django.shortcuts import render
from rest_framework import status
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_customers(request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([AllowAny]) 
def customer_create(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny]) 
def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)