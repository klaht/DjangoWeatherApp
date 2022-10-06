from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

api_key = "dd82f9fc45781a5307d640e53bfcee0d"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
url = base_url + "appid=" + api_key + "&q=" + "Oulu"
response = requests.get(url)
x = response.json()


def index(request):
    if x["cod"] != "404":
        y = x["main"]

    data = {
        'temperature': round(float(y["temp"]) - 273.15, 1),
        'pressure': float(y["pressure"]),
        'humidity': float(y["humidity"]),
    }

    return render(request, 'weather/index.html', data)
