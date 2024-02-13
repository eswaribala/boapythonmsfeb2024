from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customer.models import Customer
from customer.serializers import CustomerSerializer


# Create your views here.
@swagger_auto_schema(
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['accountNo', 'firstName', 'middleName', 'lastName', 'contactNo', 'email', 'password'],
        properties={
            'accountNo': openapi.Schema(type=openapi.TYPE_NUMBER),
            'firstName': openapi.Schema(type=openapi.TYPE_STRING),
            'middleName': openapi.Schema(type=openapi.TYPE_STRING),
            'lastName': openapi.Schema(type=openapi.TYPE_STRING),
            'contactNo': openapi.Schema(type=openapi.TYPE_NUMBER),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
            # 'end_date': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd'),

        },
    ),
    operation_description='Create Customer',
    responses={200: ""}
)
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


api_view(["GET", "PUT", "DELETE"])


def customer_parameterized_data(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(data={'The customer does not exist'}, status=400)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    