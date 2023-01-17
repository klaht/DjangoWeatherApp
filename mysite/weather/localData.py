# Create your models here.

class Week:
    def __init__(self, city):
        self.city = city
        self.days = []


class Day:
    def __init__(self, date, time, temperature, humidity, day_num, weekday, icon):
        self.date = date
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.day_num = day_num
        self.timeslots = []
        self.city = None
        self.weekday = weekday
        self.icon = icon

    def set_city(self, city):
        self.city = city

    # calculate average temperature of the whole day
    def get_avg_temp(self):
        avg_temp = 0.0
        for i in self.timeslots:
            avg_temp += i.temperature
        return round(avg_temp / len(self.timeslots), 2)


class TimeSlot:
    def __init__(self, date, time, temperature, humidity, description, icon_code, wind_speed):
        self.date = date
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.description = description
        self.icon_code = icon_code
        self.wind_speed = wind_speed
