import requests
import os
from tabulate import tabulate
from termcolor import colored
from pyfiglet import Figlet
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

    # Extract relevant weather information
    weather = data["weather"][0]["description"]
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

    # Generate ASCII art for weather symbol
    weather_symbol = data["weather"][0]["icon"]
    figlet = Figlet(font="slant")
    ascii_art = figlet.renderText(weather_symbol)

    # Display weather information in a table
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
    headers = ["", ""]
    table_str = tabulate(table, headers, tablefmt="fancy_grid")

    print(ascii_art)
    print(table_str)


def main():
    city = input("Enter the city name: ")
    print("\nFetching weather information...\n")
    get_weather(city)


if __name__ == "__main__":
    main()
