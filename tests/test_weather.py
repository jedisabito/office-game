import unittest
import json
from pkg_resources import resource_filename
from weather.weather import Weather


class TestWeather(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_weather = Weather()
        cls.test_weather.write_out()

    def test_date_converter(self):
        self.assertEqual((1, 1, 2000), self.test_weather.convert_date_to_tuple("1/1/2000"))

    def test_weather_event(self):
        with open(resource_filename(self.__module__, '../story/weather/weather.json'), 'r') as f:
            weather_data = json.loads(f.read())
            test_event = weather_data["events"][0]
            event_date = self.test_weather.convert_date_to_tuple(test_event["date"])
            self.assertEqual(self.test_weather.get_raw_weather(event_date), test_event["weather"])

    def test_random_weather(self):
        random_weather = self.test_weather.random_weather()
        self.assertIn(random_weather, self.test_weather.get_weather_types())
