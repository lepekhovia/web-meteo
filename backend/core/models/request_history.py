import uuid

from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.db import models


class RequestHistory(models.Model):

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name=_('Unique request ID'))
    town = models.CharField(max_length=100, verbose_name=_('City requested by user'))
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name=_('User'), related_name='requests')
    created_at = models.DateTimeField(default=now, verbose_name=_('Request creation date'))

    class Meta:
        verbose_name = _('Request history')
        verbose_name_plural = _('Request histories')

    def __str__(self):
        return f"Request {self.id} {self.created_at}"
