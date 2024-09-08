from main import app
from flask import render_template, request
from weather import get_weather


@app.route('/', methods=['GET'])
def index():
    return render_template('homepage.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city', '')
    weather_data = get_weather(city)
    return render_template('homepage.html', weather_data=weather_data)


@app.route("/info")
def info():
    return render_template("info.html")
