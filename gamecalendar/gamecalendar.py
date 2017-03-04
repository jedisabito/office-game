import json
from pkg_resources import resource_filename


class Month:
    def __init__(self, name, days):
        self.__name = name
        self.__days = days

    def get_name(self):
        return self.__name

    def get_days(self):
        return self.__days


class Calendar:
    def __init__(self, month=None, day=None, year=None):
        self.__MONTHS = [
            Month("January", 31),
            Month("February", 28),
            Month("March", 31),
            Month("April", 30),
            Month("May", 31),
            Month("June", 30),
            Month("July", 31),
            Month("August", 31),
            Month("September", 30),
            Month("October", 31),
            Month("November", 30),
            Month("December", 31)
        ]
        with open(resource_filename(self.__module__, '../story/calendar/calendar.json'), 'r') as f:
            calendar_data = json.loads(f.read())
            if month is None:
                self.__current_day = self.convert_date_to_dict(calendar_data["start_date"])
            else:
                self.__current_day = {
                    "month": month,
                    "day": day,
                    "year": year
                }
            self.__end_date = self.convert_date_to_dict(calendar_data["end_date"])

    @staticmethod
    def convert_date_to_dict(date):
        raw_date = date.split("/")
        return {
            "month": int(raw_date[0]),
            "day": int(raw_date[1]),
            "year": int(raw_date[2])
        }

    def its_not_the_end(self):
        return self.__current_day != self.__end_date

    def week_day(self):
        month = self.__current_day["month"]
        day = self.__current_day["day"]
        year = self.__current_day["year"]
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        week = ['Sunday',
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday']
        after_feb = 1
        if month > 2:
            after_feb = 0
        aux = year - 1700 - after_feb
        day_of_week = 5
        day_of_week += (aux + after_feb) * 365
        day_of_week += aux / 4 - aux / 100 + (aux + 100) / 400
        day_of_week += offset[month - 1] + (day - 1)
        day_of_week %= 7
        return week[day_of_week]

    def advance_day(self):
        month_end = self.__MONTHS[self.__current_day["month"] - 1].get_days()
        if self.its_february_and_leap_year():
            month_end += 1

        if month_end > self.__current_day["day"]:
            self.__current_day["day"] += 1
        else:
            self.__current_day["month"] += 1
            self.__current_day["day"] = 1

        if self.__current_day["month"] == 13:
            self.__current_day["month"] = 1
            self.__current_day["year"] += 1

    def its_february_and_leap_year(self):
        return self.__current_day["year"] % 4 == 0 and self.__current_day["month"] == 2

    def date(self):
        day_of_week_name = self.week_day()
        month_name = self.__MONTHS[self.__current_day["month"] - 1].get_name()
        day_name = str(self.__current_day["day"]) + self.date_suffix()
        year_name = str(self.__current_day["year"])
        return '''Today's Date: %s, %s %s, %s''' % (day_of_week_name, month_name, day_name, year_name)

    def raw_date(self):
        return self.__current_day["month"], self.__current_day["day"], self.__current_day["year"]

    def date_suffix(self):
        day = self.__current_day["day"]
        if day % 10 == 1 and (day < 10 or day > 20):
            return "st"
        elif self.__current_day["day"] % 10 == 2 and (day < 10 or day > 20):
            return "nd"
        elif self.__current_day["day"] % 10 == 3 and (day < 10 or day > 20):
            return "rd"
        else:
            return "th"
