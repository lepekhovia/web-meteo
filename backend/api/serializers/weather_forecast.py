from rest_framework import serializers

from core.models.weather_forecast import WeatherForecast
from api.serializers.user import UserSerializer


class WeatherForecastSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = WeatherForecast
        fields = '__all__'
