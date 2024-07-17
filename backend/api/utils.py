import requests

from config.settings import GET_FORECAST_API, GEOCODING_API


def get_weather_forecast(city, language='en'):
    geo_url = f'{GEOCODING_API}'
    geo_params  = {
        'name': city,
        'lang': language,
        }
    response_geo = requests.get(geo_url)
    print(response_geo)

    weather_params = {

        }
    response_weather = requests.get(GET_FORECAST_API, params=weather_params)

    if response_weather.status_code == 200:
        weather_data = response_weather.json()
        return weather_data
    else:
        return None
