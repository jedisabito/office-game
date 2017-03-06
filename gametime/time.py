import json
from pkg_resources import resource_filename


class Time:
    def __init__(self):
        with open(resource_filename(self.__module__, '../story/time/time.json'), 'r') as f:
            time_data = json.loads(f.read())
            self.__TIMES = time_data["times"]
        self.__current_time = 0

    def read_in(self):
        with open(resource_filename(self.__module__, '../game_data/time.json'), 'r') as f:
            time_data = json.loads(f.read())
            self.__current_time = time_data["current_time"]

    def write_out(self):
        with open(resource_filename(self.__module__, '../game_data/time.json'), 'w+') as f:
            f.write(json.dumps({
                "current_time": self.__current_time
            }))

    def get_time(self):
        self.read_in()
        return "Time: " + self.__TIMES[self.__current_time]

    def get_raw_time(self):
        self.read_in()
        return self.__current_time

    def reset(self):
        self.__current_time = 0
        self.write_out()

    def advance_time(self):
        self.read_in()
        if self.__current_time == len(self.__TIMES) - 1:
            self.reset()
        else:
            self.__current_time += 1
        self.write_out()
