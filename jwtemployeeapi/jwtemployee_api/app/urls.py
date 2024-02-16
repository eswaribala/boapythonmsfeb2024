from django.urls import path

from employee import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]