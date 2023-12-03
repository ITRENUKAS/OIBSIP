import requests
from datetime import datetime

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main_info = weather_data["main"]
        weather_info = weather_data["weather"][0]
        wind_info = weather_data["wind"]

        print(f"Weather in {city}:")
        print(f"Temperature: {main_info['temp']}°C")
        print(f"Description: {weather_info['description']}")
        print(f"Humidity: {main_info['humidity']}%")
        print(f"Wind Speed: {wind_info['speed']} m/s")
        print(f"Last Updated: {datetime.utcfromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"City not found. Error code: {weather_data['cod']}")

if __name__ == "__main__":
    api_key = "da46b98fdbf3dee8f46e46337ece8394"  # Replace with your API key
    city_name = input("Enter the city name: ")
    get_weather(api_key, city_name)


