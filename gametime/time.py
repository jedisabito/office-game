class Time:
    def __init__(self, time=None):
        self.__TIMES = [
            "Early Morning",
            "Morning",
            "Lunchtime",
            "Afternoon",
            "Dinnertime",
            "Evening"
        ]
        if time is None:
            time = 0
        self.__current_time = time

    def get_time(self):
        return self.__TIMES[self.__current_time]

    def reset(self):
        self.__current_time = 0

    def advance_time(self):
        self.__current_time += 1
