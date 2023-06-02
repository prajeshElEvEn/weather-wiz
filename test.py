import requests
from tabulate import tabulate
from termcolor import colored

API_KEY = "your-api-key"
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

    # Display weather information in a table
    table = [
        [colored("City", "green"), colored(city, "cyan")],
        [colored("Weather", "green"), colored(weather, "cyan")],
        [colored("Temperature", "green"), colored(f"{temperature}°C", "cyan")],
        [colored("Humidity", "green"), colored(f"{humidity}%", "cyan")],
    ]
    headers = ["", ""]
    table_str = tabulate(table, headers, tablefmt="fancy_grid")

    print(table_str)


def main():
    city = input("Enter the city name: ")
    print("\nFetching weather information...\n")
    get_weather(city)


if __name__ == "__main__":
    main()
