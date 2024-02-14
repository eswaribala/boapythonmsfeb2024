import requests
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from requests.auth import HTTPBasicAuth
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


@swagger_auto_schema(
    methods=['put'],
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
    operation_description='Update Customer',
    responses={200: ""}
)
@api_view(["GET", "PUT", "DELETE"])
def customer_parameterized_data(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(data={'The customer does not exist'}, status=400)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            # Customize the response for a successful creation
            response_data = {
                'message': 'Customer updated successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(data={'Customer Deleted Successfully'}, status=200)


import os
from dotenv import load_dotenv

load_dotenv()

import hvac
import sys

# Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='hvs.h4yQdfitEPcBeFzWH1o5VQFC',
)

# Reading a secret
read_response = client.secrets.kv.read_secret_version(path='basicauth')
username = read_response['data']['data']['username']
password = read_response['data']['data']['password']




@swagger_auto_schema(
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['accountNo', 'runningTotal', 'openingDate'],
        properties={
            'accountNo': openapi.Schema(type=openapi.TYPE_NUMBER),
            'runningTotal': openapi.Schema(type=openapi.TYPE_NUMBER),
            'openingDate': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd')
            # 'end_date': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd'),

        },
    ),
    operation_description='Create Account',
    responses={200: ""}
)
@api_view(["GET", "POST"])
def account_data(request):
    api_url = os.getenv("api_url")
    print(api_url)
    if request.method == 'GET':
        response = requests.get(api_url, auth=HTTPBasicAuth(username, password))
        return Response(response.json())
    elif request.method == 'POST':
        response = requests.post(api_url, auth=HTTPBasicAuth(username, password),json=request.data)
        # Customize the response for a successful creation
        response_data = {
            'message': 'Account created successfully!',
            'data': response.json(),
        }
        return Response(response_data, status=201)
