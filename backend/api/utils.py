import requests

from config.settings import GET_FORECAST_API, GEOCODING_API


def get_weather_forecast(town, language='ru'):

    params = {"name": town, "language": language}
    geo_responses = requests.get(GEOCODING_API, params=params)
    geo_responses = geo_responses.json()

    weather_forecast = {}
    for response in geo_responses['results']:
        params = {"latitude": response['latitude'], "longitude": response['longitude'], "hourly": "temperature_2m"}
        weather = requests.get(GET_FORECAST_API, params=params)
        weather = weather.json()
        weather_forecast['time'] = weather['hourly']['time'][::3]
        weather_forecast['temperature_2m'] = weather['hourly']['temperature_2m'][::3]
    return weather_forecast
