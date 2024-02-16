import socket

from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from py_eureka_client import eureka_client

from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Account
from account.serializers import AccountSerializer


# Create your views here.
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
@api_view(['GET', 'POST'])
def account_data(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            # Customize the response for a successful creation
            response_data = {
                'message': 'Account created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


