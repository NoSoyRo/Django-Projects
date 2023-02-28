from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Customer.models import Customer
from Customer.serializers import CustomerSerializer
from rest_framework.decorators import api_view

# CRUD with django:

# GET -> API/CUSTOMERS -> GET ALL CUSTOMERS   
# GET -> API/CUSTOMERS/ID -> GET CUTOMER WITH ID id 
# POST -> API/CUSTOMERS -> ADD NEW CUSTOMER 
# PUT -> API/CUSTOMERS/ID -> UPDATE CUSTOMER WITH ID id
# DELETE -> API/CUSTOMERS -> REMOVE ALL CUSTOMERS
# DELETE -> API/CUSTOMERS -> REMOVE CUSTOMER WITH ID id  

@api_view(['GET', 'POST', 'DELETE'])
def customerList(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializers = CustomerSerializer(customers, many = True)
        return JsonResponse(customers_serializers.data, safe = False)
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data = customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Customer.objects.all().delete()
        return JsonResponse({'message': '{} Customers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 


@api_view(['GET', 'PUT', 'DELETE'])
def customerDetail(request, pk):
    try: 
        customer = Customer.object.get(pk=pk) 
    except Customer.DoesNotExist: 
        return JsonResponse({'message': 'The Customer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customer_serializer = CustomerSerializer(customer) 
        return JsonResponse(customer_serializer.data) 
 
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = CustomerSerializer(Customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        customer.delete() 
        return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    