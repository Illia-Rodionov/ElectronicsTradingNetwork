from django.contrib import admin
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

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
    list_display = ['supplier_name', 'provider_link']
    list_filter = ['contact__city']
    actions = [clear_the_debt]

    def provider_link(self, obj):
        """sending to the Supplier"""
        if obj.provider:
            link = reverse(f"admin:core_supplier_change",
                           args=[obj.provider.pk])
            return mark_safe(f'<a href="{link}">{escape(obj.provider.supplier_name)}</a>')
        else:
            return obj.provider

    provider_link.allow_tags = True
    provider_link.admin_order_field = 'provider'
    provider_link.short_description = Supplier._meta.get_field('provider').verbose_name.title()
