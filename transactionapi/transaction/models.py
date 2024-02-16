from django.db import models


# Create your models here.
class Transaction(models.Model):
    transactionId = models.BigIntegerField(primary_key=True)
    amount = models.BigIntegerField(default=0)
    dot = models.DateField(null=False)
