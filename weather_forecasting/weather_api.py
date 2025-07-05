# weather_forecasting/weather_api.py
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    weather = {
        'Temperature': response['main']['temp'],
        'Humidity': response['main']['humidity'],
        'Weather': response['weather'][0]['description']
    }
    return weather
