import json
import random
from pkg_resources import resource_filename
from gamecalendar.calendar import Calendar

class Weather:
    def __init__(self):
        with open(resource_filename(self.__module__, '../story/weather/weather.json'), 'r') as f:
            weather_data = json.loads(f.read())
            events = []
            for event in weather_data["events"]:
                date = self.convert_date_to_tuple(event["date"])
                events.append({
                    "date": date,
                    "weather": event["weather"]
                })
            self.__events = events
            self.__weather_types = weather_data["weather_types"]
            self.__weather_probabilities = weather_data["weather_probabilities"]
            self.__forecast = self.generate_forecast()

    def generate_forecast(self):
        test_calendar = Calendar()
        forecast = {}
        while test_calendar.its_not_the_end_util():
            date = test_calendar.raw_date_util()
            forecast[self.convert_date_to_string(date)] = self.compute_weather(date)
            test_calendar.advance_day_util()
        return forecast

    def write_out(self):
        with open(resource_filename(self.__module__, '../game_data/forecast.json'), 'w+') as f:
            f.write(json.dumps({
                "forecast": self.__forecast
            }))

    def read_in(self):
        with open(resource_filename(self.__module__, '../game_data/forecast.json'), 'r') as f:
            forecast_data = json.loads(f.read())
            self.__forecast = forecast_data["forecast"]

    @staticmethod
    def convert_date_to_tuple(date):
        raw_date = date.split("/")
        return int(raw_date[0]), int(raw_date[1]), int(raw_date[2])

    @staticmethod
    def convert_date_to_string(date):
        return str(date[0]) + "/" + str(date[1]) + "/" + str(date[2])

    def compute_weather(self, date):
        for event in self.__events:
            if event["date"] == date:
                return event["weather"]
        return self.random_weather()

    def get_weather(self, date):
        self.read_in()
        return "Weather: " + self.get_raw_weather(date)

    def get_raw_weather(self, date):
        self.read_in()
        return self.__forecast[self.convert_date_to_string(date)]

    def get_weather_types(self):
        return self.__weather_types

    def random_weather(self):
        random.seed()
        rand = random.random()
        total = 0
        for i in range(len(self.__weather_probabilities)):
            total += self.__weather_probabilities[i]
            if total >= rand:
                return self.__weather_types[i]
