from libs.openweathermap import CurrentWeather, HistoricalWeatherData
from datetime import datetime

API_KEY = "813a7ac588302e96a5b068466ae2944f"

USER_CHOICE = """Enter:
- 'coord' to know the coordinates
- 'weather' to know the current weather
- 'main' to know the temperature
- 'visibility' to know the visibility
- 'wind' for information of the wind
- 'hd' for Data from the last 5 days
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'coord' or user_input == 'weather' \
                or user_input == 'main' or user_input == 'visibility' or user_input == 'wind':
            print_current_information(user_input)
        elif user_input == 'hd':
            print_historical_data()
        else:
            print("Unknown command! Please try again")
        user_input = input(USER_CHOICE)


def print_current_information(user_input):
    city_name = input("Enter the city you want to have information from: ")
    current_weather = CurrentWeather(API_KEY, city_name).latest()
    return print(current_weather[user_input])


def print_historical_data():
    city_lat = input("Enter the latitude of the city you want to have information from: ")
    city_lon = input("Enter the longitude of the city you want to have information from: ")
    day = int(input("Enter from what day you want the information: "))
    historical_weather = HistoricalWeatherData(API_KEY, city_lat, city_lon, convert_time(2021, 1, day))
    return print(historical_weather.latest())


def convert_time(year, month, day):
    dt = datetime(year, month, day)
    ts = int(datetime.timestamp(dt))
    return ts


menu()
