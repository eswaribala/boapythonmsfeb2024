"""
URL configuration for customer_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys

import requests
from django.contrib import admin
from django.http import HttpRequest
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

import customer_api.urls
from customer.views import customer_data, customer_parameterized_data, account_data

schema_view = get_schema_view(
    openapi.Info(
        title="Customer API",
        default_version='v1', ),
    public=True,
    permission_classes=([permissions.AllowAny])
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/v1.0/', customer_data),
    path('customers/v1.0/<int:pk>/', customer_parameterized_data),
    path('accounts/v1.0/', account_data),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

import py_eureka_client.eureka_client as eureka_client
import socket
requestMeta=socket.gethostbyname(socket.gethostname())+","+sys.argv[2]
print(requestMeta)
meta = requestMeta.split(',')
print(meta[1])
your_rest_server_port = int(meta[1])
hostName = socket.gethostbyaddr('127.0.0.1')
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init(eureka_server="http://localhost:8761",
                   app_name="Customer-App",
                   instance_ip='localhost',
                   instance_host='localhost',
                   instance_port=your_rest_server_port)

