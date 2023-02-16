from rest_framework import serializers

from core.models import Supplier, Product, User


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        model = User
        fields = ('username',)


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""
    class Meta:
        model = Product
        fields = ('name', 'product_model', 'market_launch_date')


class SupplierSerializer(serializers.ModelSerializer):
    """Supplier Serializer"""
    debt_to_the_supplier = serializers.FloatField(read_only=True)

    class Meta:
        model = Supplier
        fields = ('supplier_name', "supplier_type", 'contact', 'email', 'product', 'employee', 'provider',
                  'debt_to_the_supplier', 'created_at')


class SupplierStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('supplier_name', "supplier_type", 'debt_to_the_supplier', 'provider')

        depth = 1