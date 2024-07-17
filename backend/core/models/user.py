import uuid

from django.utils.translation import gettext_lazy as _
from django.db import models


class User(models.Model):

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name=_('Unique user ID'))
    town = models.CharField(max_length=100, verbose_name=_('Last city requested by user'))

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f"User {self.id}"
