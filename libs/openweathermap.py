import requests


class CurrentWeather:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, app_key, city_name):
        self.app_key = app_key
        self.city_name = city_name

    def latest(self):
        return requests.get(f"{self.BASE_URL}q={self.city_name}&appid={self.app_key}").json()
