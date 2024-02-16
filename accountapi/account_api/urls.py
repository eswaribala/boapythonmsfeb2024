"""
URL configuration for account_api project.

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

from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from py_eureka_client import eureka_client
from rest_framework import permissions

from account.views import account_data

schema_view = get_schema_view(
    openapi.Info(
        title="Account API",
        default_version='v1', ),
    public=True,
    permission_classes=([permissions.AllowAny])
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/v1.0/', account_data),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]



#import socket
#requestMeta=socket.gethostbyname(socket.gethostname())+","+sys.argv[4]
#print(requestMeta)
#meta = requestMeta.split(':')
#print(meta[1])

# import docker
# client = docker.from_env()
# container = client.containers.run("account_api", "sleep 5000", detach=True)
# container.reload()  # required to get auto-assigned ports, not needed if it was an already running container
# print(container.ports)

#your_rest_server_port = 8000
#hostName = socket.gethostbyaddr('127.0.0.1')
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
#eureka_client.init(eureka_server="http://host.docker.internal:8761",
#                   app_name="Account-App",
#                   instance_ip='127.0.0.1',
#                   instance_host='127.0.0.1',
#                   instance_port=your_rest_server_port)