import json
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view
from rest_framework.response import Response

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer



import os
from dotenv import load_dotenv

load_dotenv()


# Create your views here.
@swagger_auto_schema(
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['transactionId', 'amount', 'dot'],
        properties={
            'transactionId': openapi.Schema(type=openapi.TYPE_NUMBER),
            'amount': openapi.Schema(type=openapi.TYPE_NUMBER),
            'dot': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd')
            # 'end_date': openapi.Schema(type=openapi.TYPE_STRING, default='yyyy-mm-dd'),

        },
    ),
    operation_description='Create Transaction',
    responses={200: ""}
)
@api_view(['GET', 'POST'])
def transaction_data(request):
    if request.method == 'GET':

        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            jsonData = json.dumps(serializer.data)

            # Customize the response for a successful creation
            response_data = {
                'message': 'Transaction created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
