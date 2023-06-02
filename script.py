import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)

        if data["cod"] == "404":
            print("City not found.")
        else:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"Weather: {weather}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("An error occurred while retrieving the weather data.")
        print(e)


def main():
    city = input("Enter the city name: ")
    api_key = os.environ.get("OPEN_WEATHER_API_KEY")

    get_weather(city, api_key)


if __name__ == "__main__":
    main()
