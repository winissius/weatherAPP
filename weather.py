# weather.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv('API_KEY')


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang=pt_br&units=metric'
    response = requests.get(url)
    data = response.json()

    if data.get('cod') == 200:
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather = data['weather'][0]['main']
        return {
            'city': data['name'],
            'country': country,
            'temperature': temperature,
            'weather': weather
        }
    else:
        return {'error': 'City not found'}
