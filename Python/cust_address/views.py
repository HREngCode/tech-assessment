from django.shortcuts import render
from rest_framework import status
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Address
from .serializers import AddressSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_addresses(request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([AllowAny]) 
def address_create(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny]) 
def address_detail(request, pk):
    address = Address.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        except Address.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = AddressSerializer(address, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)