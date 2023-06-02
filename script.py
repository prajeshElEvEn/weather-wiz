import requests
import os
from tabulate import tabulate
from termcolor import colored
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


def get_weather(city):
    url = API_URL.format(city=city, api_key=API_KEY)
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print(colored(f"Error: {data['message']}", "red"))
        return

    weather = data["weather"][0]["description"]
    weather = weather.capitalize()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    max_temp = data["main"]["temp_max"]
    min_temp = data["main"]["temp_min"]
    feels_like = data["main"]["feels_like"]
    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"]).strftime("%H:%M:%S")
    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")
    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]

    table = [
        [colored("City", "green"), colored(city, "cyan")],
        [colored("Weather", "green"), colored(weather, "cyan")],
        [colored("Temperature", "green"), colored(f"{temperature}°C", "cyan")],
        [colored("Humidity", "green"), colored(f"{humidity}%", "cyan")],
        [colored("Wind Speed", "green"), colored(f"{wind_speed} m/s", "cyan")],
        [colored("Max Temperature", "green"),
         colored(f"{max_temp}°C", "cyan")],
        [colored("Min Temperature", "green"),
         colored(f"{min_temp}°C", "cyan")],
        [colored("Feels Like", "green"), colored(f"{feels_like}°C", "cyan")],
        [colored("Sunrise", "green"), colored(f"{sunrise}", "cyan")],
        [colored("Sunset", "green"), colored(f"{sunset}", "cyan")],
        [colored("Latitude", "green"), colored(f"{lat}°", "cyan")],
        [colored("Longitude", "green"), colored(f"{lon}°", "cyan")],
    ]

    table_str = tabulate(table, tablefmt="fancy_grid")

    print(table_str)


def main():
    print(colored("-----------------------------------------------------------", "green"))
    print(colored("WeatherWiz - Weather Forecast Python CLI Tool", "blue"))
    print(colored("-----------------------------------------------------------", "green"))
    print("")
    city = input(
        colored("Enter a city name(such as: New Delhi, New York)\n> ", "magenta"))
    city = city.capitalize()
    print("")
    print(colored(f"Retrieving weather information for {city}...", "yellow"))
    print("")
    get_weather(city)
    print("")
    print(colored("-----------------------------------------------------------", "green"))
    print(colored("Thank you for using WeatherWiz!", "blue"))
    print(colored("-----------------------------------------------------------", "green"))


if __name__ == "__main__":
    main()
