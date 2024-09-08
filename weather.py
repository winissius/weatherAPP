import requests
import os
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv('API_KEY')

city = 'Curitiba'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang=pt_br&units=metric'


def get_weather(url):
    response = requests.get(url)
    data = response.json()
    country = data['sys']['country']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['main']
    print(f' Weather in {data['name']}-{country} right now!')
    print(f' {weather} weather')
    print(f' Temperature: {temperature} oC')
    print(f' Humidity: {humidity}%')
    # print(json.dumps(data, indent=4, ensure_ascii=False))


get_weather(url)


