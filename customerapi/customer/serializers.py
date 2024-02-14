from packaging.metadata import Metadata
from rest_framework import  serializers

from customer.models import Customer, Individual, Corporate


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = '__all__'


class CorporateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate
        fields = '__all__'
