from django.db import models


# Create your models here.
class Account(models.Model):
    accountNo = models.BigIntegerField(primary_key=True)
    runningTotal = models.BigIntegerField(default=0)
    openingDate = models.DateField(null=False)


class SavingsAccount(Account):
    interestRate = models.FloatField(default=0.0)


class CurrentAccount(Account):
    odLimit = models.BigIntegerField(default=0)