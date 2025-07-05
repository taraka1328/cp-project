# weather_forecasting/weather_api.py
import requests

def get_weather(city, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code != 200:
            return {
                'error': f"Weather API request failed with status {response.status_code}. Please check your API key and city name."
            }
        
        data = response.json()
        
        # Check if the response has the expected structure
        if 'main' not in data or 'weather' not in data:
            return {
                'error': "Unexpected weather API response format."
            }
        
        weather = {
            'Temperature': data['main']['temp'],
            'Humidity': data['main']['humidity'],
            'Weather': data['weather'][0]['description']
        }
        return weather
        
    except requests.exceptions.RequestException as e:
        return {
            'error': f"Network request failed: {str(e)}"
        }
    except KeyError as e:
        return {
            'error': f"Missing data in weather response: {str(e)}"
        }
    except Exception as e:
        return {
            'error': f"Weather API error: {str(e)}"
        }
