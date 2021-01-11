from libs.openweathermap import CurrentWeather, StatisticalWeatherData

API_KEY = "813a7ac588302e96a5b068466ae2944f"
city_name = input("Enter the city you want to have information from: ")
current_weather = CurrentWeather(API_KEY, city_name).latest()

USER_CHOICE = """Enter:
- 'coord' to know the coordinates
- 'weather' to know the current weather
- 'main' to know the temperature
- 'visibility' to know the visibility
- 'wind' for information of the wind
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        print_information(user_input)
        user_input = input(USER_CHOICE)


def print_information(user_input):
    return print(current_weather[user_input])


# menu()

stat_weather_data = StatisticalWeatherData(API_KEY, city_name).latest()
print(stat_weather_data)
