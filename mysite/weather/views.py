from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CityForm
import requests
import json

api_key = "dd82f9fc45781a5307d640e53bfcee0d"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
default_city = "Helsinki"
url = base_url + "appid=" + api_key + "&q=" + default_city
response = requests.get(url)
x = response.json()


def index(request):
    if x["cod"] != "404":
        y = x["main"]

    data = {
        'city': default_city,
        'temperature': round(float(y["temp"]) - 273.15, 1),
        'pressure': float(y["pressure"]),
        'humidity': float(y["humidity"])
    }

    return render(request, 'weather/index.html', data)


def submit_city(request):

    if request.method == 'GET':
        form = CityForm(request.GET)

        if form.is_valid():

            city = form.cleaned_data.get("city")

            url = base_url + "appid=" + api_key + "&q=" + city
            response = requests.get(url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
            else:
                return render(request, 'weather/error.html')


            data = {
                'city': city,
                'temperature': round(float(y["temp"]) - 273.15, 1),
                'pressure': float(y["pressure"]),
                'humidity': float(y["humidity"])
            }

            return render(request, 'weather/index.html', data)

    return HttpResponse("Error")
