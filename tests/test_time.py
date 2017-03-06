import unittest
import json
from pkg_resources import resource_filename
from gametime.time import Time


class TestTime(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_time = Time()
        cls.test_time.write_out()
        with open(resource_filename(cls.__module__, '../game_data/time.json'), 'r') as f:
            cls.time_data = json.loads(f.read())

    def read_in(self):
        with open(resource_filename(self.__module__, '../game_data/time.json'), 'r') as f:
            return json.loads(f.read())

    def test_a_write_current_time(self):
        self.assertEqual(self.time_data['current_time'], self.test_time.get_raw_time())

    def test_b_advance_time(self):
        self.test_time.advance_time()
        self.time_data = self.read_in()
        self.assertEqual(self.time_data["current_time"], 1)

    def test_c_reset_time(self):
        with open(resource_filename(self.__module__, '../story/time/time.json'), 'r') as f:
            times_data = json.loads(f.read())
            for i in range(len(times_data["times"]) - self.test_time.get_raw_time()):
                self.test_time.advance_time()
            self.time_data = self.read_in()
            self.assertEqual(self.time_data["current_time"], 0)
