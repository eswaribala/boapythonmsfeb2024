from rest_framework import serializers

from account.models import Account, SavingsAccount, CurrentAccount


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class SavingsAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsAccount
        fields = '__all__'


class CurrentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentAccount
        fields = '__all__'
