import json
import random
from pkg_resources import resource_filename


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

    @staticmethod
    def convert_date_to_tuple(date):
        raw_date = date.split("/")
        return int(raw_date[0]), int(raw_date[1]), int(raw_date[2])

    def get_weather(self, date):
        for event in self.__events:
            if event["date"] == date:
                return "Weather: " + event["weather"]
        return "Weather: " + self.random_weather()

    def get_raw_weather(self, date):
        for event in self.__events:
            if event["date"] == date:
                return event["weather"]
        return self.random_weather()

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