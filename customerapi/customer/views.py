from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customer.models import Customer
from customer.serializers import CustomerSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def customer_data(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            # Customize the response for a successful creation
            response_data = {
                'message': 'Customer created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


