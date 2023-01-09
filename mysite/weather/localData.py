# Create your models here.

class Week:
    def __init__(self, city):
        self.city = city
        self.days = []


class Day:
    def __init__(self, date, time, temperature, humidity, day_num):
        self.date = date
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.day_num = day_num
        self.timeslots = []
        self.city = None

    def set_city(self, city):
        self.city = city


class TimeSlot:
    def __init__(self, date, time, temperature, humidity, description, icon_code):
        self.date = date
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.description = description
        self.icon_code = icon_code
