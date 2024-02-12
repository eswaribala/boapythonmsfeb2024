from django.db import models


# Create your models here.

class Customer(models.Model):
    accountNo = models.IntegerField(primary_key=True)
    firstName = models.TextField(null=False)
    middleName = models.TextField(null=True)
    lastName = models.TextField(null=False)


# class FullName:
#     firstName = models.TextField(null=False)
#     middleName = models.TextField(null=True)
#     lastName = models.TextField(null=False)

class Address(models.Model):
    addressId = models.IntegerField(primary_key=True)
    doorNo = models.TextField(null=False)
    streetName = models.TextField(null=False)
    city = models.TextField(null=False)
    pincode = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
