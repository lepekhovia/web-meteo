from django.contrib import admin
from core.models.user import User
from core.models.request_history import RequestHistory
from core.models.weather_forecast import WeatherForecast


admin.site.register(User)
admin.site.register(RequestHistory)
admin.site.register(WeatherForecast)
