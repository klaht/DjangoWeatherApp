from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import requests
from .forms import CityForm
import json

from .localData import Week, Day, TimeSlot

api_key = "dd82f9fc45781a5307d640e53bfcee0d"


def index(request):
    return render(request, 'weather/index.html')


def organize_API_data(city):
    week = Week(city)

    forecast_data = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(forecast_data)
    data_json = response.json()
    #print(data_json["list"][0]["weather"][0]["main"])

    if data_json["cod"] != "404":
        i = 0
        current_day = data_json["list"][0]["dt_txt"][5:10]
        day_index = 0

        # fill the local week data structure with the data from the api
        for day_num in range(6):
            day = Day(data_json["list"][i]["dt_txt"].split()[0],
                      data_json["list"][i]["dt_txt"].split()[1],
                      data_json["list"][i]["main"]["temp"],
                      data_json["list"][i]["main"]["humidity"], day_num + 1)
            week.days.append(day)
            while i < len(data_json["list"]):
                if data_json["list"][i]["dt_txt"][5:10] == current_day:
                    time_slot = TimeSlot(data_json["list"][i]["dt_txt"].split()[0],
                                         data_json["list"][i]["dt_txt"].split()[1][0:5],
                                         data_json["list"][i]["main"]["temp"],
                                         data_json["list"][i]["main"]["humidity"],
                                         data_json["list"][i]["weather"][0]["main"],
                                         data_json["list"][i]["weather"][0]["icon"])
                    day.timeslots.append(time_slot)
                    i += 1
                    day_index += 1
                else:
                    current_day = data_json["list"][i]["dt_txt"][5:10]
                    break
        return week

    return HttpResponse("Error")


def week_view(request):
    if request.method == 'GET':

        form = CityForm(request.GET)

        if form.is_valid():
            # organize api data from user inputted city into a variable "week"
            city = form.cleaned_data.get("city").capitalize()
            week = organize_API_data(city)

            request.session['city'] = city

            return render(request, 'weather/week.html', {'week': week})

    return render(request, 'weather/error.html')


def day_view(request, pk, graph, slot):
    if request.method == 'GET':
        city = request.session.get('city')

        week = organize_API_data(city)

        day = week.days[pk - 1]
        currently_shown_slot = day.timeslots[slot]
        day.set_city(city)
        if graph == "t":

            day_data = [['Time', 'Temperature']]

            for current_slot in day.timeslots:
                day_data.append([current_slot.time, current_slot.temperature])
        else:
            day_data = [['Time', 'Humidity']]

            for day_slot in day.timeslots:
                day_data.append([day_slot.time, day_slot.humidity])


        return render(request, 'weather/day.html', {'day': day, 'hourValues': day_data, 'slot': currently_shown_slot, 'graph_url': graph})

    return render(request, 'weather/error.html')
