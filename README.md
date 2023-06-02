# WeatherWiz

WeatherWiz is a command-line tool that allows you to retrieve the weather forecast for a specific city using the OpenWeather API.

![WeatherWiz](/assets/images/weather-wiz.png?raw=true, "WeatherWiz")

## Installation

- Fork and clone this [repository](https://github.com/prajeshElEvEn/weather-wiz)

```bash
git clone <repo_url>
```

- Navigate to the project directory

```bash
cd weather-wiz
```

- Create a virtual environment

```bash
python3 -m venv venv
```

- Activate the virtual environment

```bash
source venv/bin/activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```

- Create a file `.env` in the root directory and add the following environment variables

```bash
OPEN_WEATHER_API_KEY=<your_api_key>
```

## Usage

- Run the following command to get the weather forecast for a specific city

```bash
python3 script.py
```

- Enter the city name when prompted

```bash
Enter the city name:
> <city_name>
```

## Authors

- [@pranjal](https://github.com/PranjalAgarwal04)
- [@prajesh](https://bit.ly/prajesheleven)
