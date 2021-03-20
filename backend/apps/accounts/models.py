from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.utils.translation import ugettext_lazy as _


class CustomUser(TenantMixin):
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    username = None
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

class Domain(DomainMixin):
    pass