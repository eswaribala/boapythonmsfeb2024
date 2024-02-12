from django.db import models


# Create your models here.

class Customer(models.Model):
    accountNo = models.IntegerField(primary_key=True)
    firstName = models.TextField(null=False, max_length=50)
    middleName = models.TextField(null=True, max_length=50)
    lastName = models.TextField(null=False, max_length=50)
    contactNo = models.IntegerField(default=0)
    email = models.TextField(max_length=150, null=False)
    password = models.TextField(max_length=10, null=False)


# class FullName:
#     firstName = models.TextField(null=False)
#     middleName = models.TextField(null=True)
#     lastName = models.TextField(null=False)

class Address(models.Model):
    addressId = models.IntegerField(primary_key=True)
    doorNo = models.TextField(null=False, max_length=5)
    streetName = models.TextField(null=False, max_length=100)
    city = models.TextField(null=False, max_length=100)
    pincode = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Gender(models.TextChoices):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    TRANSGENDER = 'TRANSGENDER'


class Individual(Customer):
    gender = models.TextField(
        choices=Gender.choices,
        default=Gender.MALE
    )
    dob = models.DateField


class CompanyType(models.TextChoices):
    GOVERNMENT = 'GOVERNMENT'
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'
    NGO = 'NGO'


class Corporate(Customer):
    companyType = models.TextField(
        choices=CompanyType.choices,
        default=CompanyType.PRIVATE
    )
