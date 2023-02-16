from django_filters import rest_framework as filters
from core.models import Supplier


class SupplierCountryFilter(filters.FilterSet):
    """Information about objects of a certain country filter by name"""
    contact = filters.CharFilter(field_name='contact__country')
    product = filters.NumberFilter(field_name='product__id')

    class Meta:
        model = Supplier
        fields = ('contact', 'product')
