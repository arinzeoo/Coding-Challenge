import requests
from flask import Flask, request

import os
app = Flask(__name__)


@app.route('/', methods=["POST"])
def search_city():
    API_KEY = os.environ['current_weather_api']  # This will retrive the key stored in my system enviroment virables.

    city = request.form.get('text')  # city name passed as form

    # This will call API and convert response into Python dictionary
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()

    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    #This will get current temperature and convert it into Celsius
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return f'Current temperature of {city.title()} is {current_temperature_celsius}C;'

if __name__ == '__main__':
    app.run(debug=True)
