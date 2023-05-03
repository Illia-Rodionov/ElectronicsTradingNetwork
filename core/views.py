from django.db.models import Avg
from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from core.models import Supplier, Product, User, Contact
from core.permissions import IsActive
from core.serializers import SupplierSerializer, ProductSerializer, \
    SupplierStatisticSerializer, UserSerializer, ContactSerializer,\
    SupplierUpdateSerializer
from core.services import SupplierCountryFilter
from core.pagination import ProductPagination


class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsActive,)


class SupplierListCreateAPIView(generics.ListCreateAPIView):
    """Supplier List Create APIView"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SupplierCountryFilter
    permission_classes = (IsActive,)


class SupplierUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Supplier Update, Delete APIView"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializer
    permission_classes = (IsActive,)


class SupplierStatisticView(generics.ListAPIView):
    """Supplier Statistic View"""
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
    pagination_class = ProductPagination


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActive, )
