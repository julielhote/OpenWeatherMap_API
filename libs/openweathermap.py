import requests


class CurrentWeather:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, api_key, city_name):
        self.api_key = api_key
        self.city_name = city_name

    def latest(self):
        return requests.get(f"{self.BASE_URL}q={self.city_name}&appid={self.api_key}").json()


class HistoricalWeatherData:
    BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine?"

    def __init__(self, api_key, lat, lon, time):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.time = time

    def latest(self):
        return requests.get(f"{self.BASE_URL}lat={self.lat}&lon={self.lon}&dt={self.time}&appid={self.api_key}").json()
