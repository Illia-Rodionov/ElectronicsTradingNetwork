from django.contrib import admin

from core.models import Product, User, Supplier, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.action(description='Clearing debts')
def clear_the_debt(modeladmin, request, queryset):
    """action to clear debt"""
    queryset.update(debt_to_the_supplier=0)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    actions = [clear_the_debt]
