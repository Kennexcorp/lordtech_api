from rest_framework import serializers

from sales.models import (
    Configuration,
    DataPlan,
    DataSubscription,
    Product,
    SalesRep
)


class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuration
        fields = '__all__'


class SalesRepSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesRep
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class DataSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSubscription
        fields = '__all__'


class DataPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataPlan
        fields = '__all__'
