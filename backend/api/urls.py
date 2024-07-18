from django.urls import path

from api.views.weather_forecast import WeatherForecastStartView, RequestWeatherForecast
from api.views.statistic import TownsStatistic


urlpatterns = [
    path('weather_start/', WeatherForecastStartView.as_view(), name='weather_start'),
    path('request_weather/', RequestWeatherForecast.as_view(), name='request_weather'),
    path('towns_statistic/', TownsStatistic.as_view(), name='towns_statistic'),
]
