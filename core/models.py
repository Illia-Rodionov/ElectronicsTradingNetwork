from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    """Contact model"""
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.IntegerField()

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street} - {self.house_number}"


class Product(models.Model):
    """Product model"""
    product_name = models.CharField(max_length=150)
    product_model = models.CharField(max_length=255)
    market_launch_date = models.DateField()

    def __str__(self):
        return self.product_name


class Supplier(models.Model):
    """Supplier model"""
    FACTORY = 1
    DISTRIBUTOR = 2
    DEALERSHIP = 3
    LARGE_RETAIL_CHAIN = 4
    INDIVIDUAL_ENTREPRENEUR = 5

    SUPPLIER_TYPES = ((FACTORY, "Factory"),
                      (DISTRIBUTOR, "Distributor"),
                      (DEALERSHIP, "Dealership"),
                      (LARGE_RETAIL_CHAIN, "Large_retail_chain"),
                      (INDIVIDUAL_ENTREPRENEUR, 'Individual_entrepreneur')
                      )

    supplier_type = models.PositiveSmallIntegerField(choices=SUPPLIER_TYPES, default=FACTORY,)
    supplier_name = models.CharField(max_length=255)
    contact = models.ManyToManyField(Contact, related_name='supplier_contact')
    email = models.EmailField(unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='supplier_product')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_employee')
    provider = models.ForeignKey('self', on_delete=models.CASCADE,
                                 blank=True, null=True, related_name='supplier_provider')
    debt_to_the_supplier = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.supplier_name
