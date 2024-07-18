import uuid

from django.utils.translation import gettext_lazy as _
from django.db import models


class User(models.Model):

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name=_('Unique user ID'))
    cookie_token = models.CharField(editable=False, verbose_name=_('Cookie key'), unique=True)
    town = models.CharField(max_length=100, verbose_name=_('Last city requested by user'))
    locale = models.CharField(max_length=10, verbose_name=_('User locale'))

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f"User {self.id}"
