from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CityForm
import requests
import json

api_key = "dd82f9fc45781a5307d640e53bfcee0d"


def index(request):
    return render(request, 'weather/index.html')


def week_view(request):
    if request.method == 'GET':

        form = CityForm(request.GET)

        if form.is_valid():

            # user inputted city
            city = form.cleaned_data.get("city").capitalize()

            # set current session city
            request.session['city'] = city

            # get city forecast data
            forecast_data = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
            response = requests.get(forecast_data)
            data_json = response.json()

            if data_json["cod"] == "404":
                return render(request, 'weather/error.html')

            day1 = {"date": data_json["list"][0]["dt_txt"], "temp": data_json["list"][0]["main"]["temp"],
                    "humidity": data_json["list"][0]["main"]["humidity"]}

            day2 = {"date": data_json["list"][8]["dt_txt"], "temp": data_json["list"][8]["main"]["temp"],
                    "humidity": data_json["list"][8]["main"]["humidity"]}

            day3 = {"date": data_json["list"][16]["dt_txt"], "temp": data_json["list"][16]["main"]["temp"],
                    "humidity": data_json["list"][16]["main"]["humidity"]}

            day4 = {"date": data_json["list"][24]["dt_txt"], "temp": data_json["list"][24]["main"]["temp"],
                    "humidity": data_json["list"][24]["main"]["humidity"]}

            day5 = {"date": data_json["list"][32]["dt_txt"], "temp": data_json["list"][32]["main"]["temp"],
                    "humidity": data_json["list"][32]["main"]["humidity"]}

            data = {"city": city,
                    "day1": day1,
                    "day2": day2,
                    "day3": day3,
                    "day4": day4,
                    "day5": day5}

            return render(request, 'weather/week.html', data)

    return render(request, 'weather/error.html')


def day_view(request, pk):

    if request.method == 'GET':

        city = request.session.get('city')

        forecast_data = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
        response = requests.get(forecast_data)
        data_json = response.json()

        # set timeslot index to i (day 1 = index 0-7, day 2 = index 8-15, etc)
        i = pk * 8 - 8

        timeslot1 = {"time": str.split(data_json["list"][i]["dt_txt"]),
                     "temp": data_json["list"][i]["main"]["temp"],
                     "humidity": data_json["list"][i]["main"]["humidity"]}

        timeslot2 = {"time": str.split(data_json["list"][i + 1]["dt_txt"]),
                     "temp": data_json["list"][i + 1]["main"]["temp"],
                     "humidity": data_json["list"][i + 1]["main"]["humidity"]}

        timeslot3 = {"time": str.split(data_json["list"][i + 2]["dt_txt"]),
                     "temp": data_json["list"][i + 2]["main"]["temp"],
                     "humidity": data_json["list"][i + 2]["main"]["humidity"]}

        timeslot4 = {"time": str.split(data_json["list"][i + 3]["dt_txt"]),
                     "temp": data_json["list"][i + 3]["main"]["temp"],
                     "humidity": data_json["list"][i + 3]["main"]["humidity"]}

        timeslot5 = {"time": str.split(data_json["list"][i + 4]["dt_txt"]),
                     "temp": data_json["list"][i + 4]["main"]["temp"],
                     "humidity": data_json["list"][i + 4]["main"]["humidity"]}

        timeslot6 = {"time": str.split(data_json["list"][i + 5]["dt_txt"]),
                     "temp": data_json["list"][i + 5]["main"]["temp"],
                     "humidity": data_json["list"][i + 5]["main"]["humidity"]}

        timeslot7 = {"time": str.split(data_json["list"][i + 6]["dt_txt"]),
                     "temp": data_json["list"][i + 6]["main"]["temp"],
                     "humidity": data_json["list"][i + 6]["main"]["humidity"]}

        timeslot8 = {"time": str.split(data_json["list"][i + 7]["dt_txt"]),
                     "temp": data_json["list"][i + 7]["main"]["temp"],
                     "humidity": data_json["list"][i + 7]["main"]["humidity"]}

        #url back to week page
        url = "/weather/city/?city=" + city

        data = {
            "city": city,
            "url": url,
            "slot1": timeslot1,
            "slot2": timeslot2,
            "slot3": timeslot3,
            "slot4": timeslot4,
            "slot5": timeslot5,
            "slot6": timeslot6,
            "slot7": timeslot7,
            "slot8": timeslot8
        }

        return render(request, 'weather/day.html', data)

    return render(request, 'weather/error.html')
