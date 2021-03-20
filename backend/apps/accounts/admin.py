from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import CustomUser, Domain

@admin.register(CustomUser)
class CustomUserAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'paid_until')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
        pass 