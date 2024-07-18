import uuid

from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.db import models


class WeatherForecast(models.Model):

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name=_('Unique forecast ID'))
    forecast = models.TextField(verbose_name=_('Weather forecast'))
    town = models.CharField(max_length=100, verbose_name=_('Town for which the forecast was requested'))
    created_at = models.DateTimeField(default=now, verbose_name=_('Forecast creation date'))
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name=_('User'), related_name='forecasts')

    class Meta:
        verbose_name = _('Weather forecast')
        verbose_name_plural = _('Weather forecasts')

    def __str__(self):
        return f"Forecast {self.id} {self.created_at}"
