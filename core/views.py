from django.db.models import Avg
from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from core.models import Supplier, Product, User, Contact
from core.permissions import IsActive
from core.serializers import SupplierSerializer, ProductSerializer, \
    SupplierStatisticSerializer, UserSerializer, ContactSerializer
from core.services import SupplierCountryFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsActive,)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SupplierCountryFilter
    permission_classes = (IsActive,)


class SupplierStatisticView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierStatisticSerializer
    permission_classes = (IsActive,)

    def get_queryset(self):
        """View to get statistics about objects whose debt exceeds the average debt all objects"""
        get_the_average = Supplier.objects.all().aggregate(Avg('debt_to_the_supplier'))
        return Supplier.objects.filter(debt_to_the_supplier__gte=get_the_average['debt_to_the_supplier__avg'])


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActive, )
