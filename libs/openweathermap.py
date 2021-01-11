import requests


class CurrentWeather:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, api_key, city_name):
        self.api_key = api_key
        self.city_name = city_name

    def latest(self):
        return requests.get(f"{self.BASE_URL}q={self.city_name}&appid={self.api_key}").json()
