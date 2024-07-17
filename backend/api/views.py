from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from core.models.request_history import RequestHistory
from core.models.user import User
from .serializers import RequestHistorySerializer
from .pagination import ListedPagination


class WeatherForecast(GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    model = RequestHistory
    queryset = RequestHistory.objects.all()
    serializer_class = RequestHistorySerializer
    pagination_class = ListedPagination
    lookup_field = 'id'
    lookup_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        print(request.session.keys())
        return render(request, 'weather_form.html')


# def weather_forecast(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         weather_data = get_weather_forecast(city, language='en')
#
#         if weather_data:
#             return render(request, 'weather_forecast.html', {'weather_data': weather_data})
#         else:
#             return render(request, 'error.html')
#
#     return render(request, 'weather_form.html')
