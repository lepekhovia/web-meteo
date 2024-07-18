from datetime import timedelta

from django.utils import timezone
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from core.models.user import User
from core.models.weather_forecast import WeatherForecast
from core.models.request_history import RequestHistory
from api.serializers.weather_forecast import WeatherForecastSerializer
from api.utils import get_weather_forecast


class WeatherForecastStartView(GenericAPIView, mixins.RetrieveModelMixin):
    model = WeatherForecast
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        try:
            user = User.objects.get(cookie_token=self.request.headers['Cookie'])
            if user.town and WeatherForecast.objects.filter(user=user, town=user.town, created_at__gte=(timezone.now()-timedelta(days=1))).exists():
                return WeatherForecast.objects.filter(user=user, town=user.town, created_at__gte=(timezone.now()-timedelta(days=1))).first()
            else:
                return None
        except User.DoesNotExist:
            User.objects.create(cookie_token=self.request.headers['Cookie'], locale=self.request.headers['Accept-Language'].split(',')[0].split(';')[0][:2].lower())
            return None


class RequestWeatherForecast(GenericAPIView, mixins.CreateModelMixin):
    model = WeatherForecast
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

    def post(self, request, *args, **kwargs):
        town = self.request.query_params.get('town')
        user = User.objects.get(cookie_token=request.headers['Cookie'])
        user.town = town
        user.save(update_fields=['town'])
        weather_data = get_weather_forecast(town, user.locale)
        if weather_data:
            WeatherForecast.objects.create(user=user, town=town, forecast=weather_data)
            RequestHistory.objects.create(user=user, town=town)
            return Response(status=status.HTTP_201_CREATED, data=weather_data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Weather forecast not found"})
