import unittest
from gamecalendar.calendar import Calendar


class TestCalendar(unittest.TestCase):

    def test_advance_day(self):
        test_calendar = Calendar(1, 1, 2000)
        test_calendar.write_out()
        test_calendar.advance_day()
        self.assertEqual("Today's Date: Sunday, January 2nd, 2000", test_calendar.date())

    def test_advance_month(self):
        test_calendar = Calendar(1, 31, 2000)
        test_calendar.write_out()
        test_calendar.advance_day()
        self.assertEqual("Today's Date: Tuesday, February 1st, 2000", test_calendar.date())

    def test_advance_year(self):
        test_calendar = Calendar(12, 31, 2000)
        test_calendar.write_out()
        test_calendar.advance_day()
        self.assertEqual("Today's Date: Monday, January 1st, 2001", test_calendar.date())

    def test_advance_leap_year(self):
        test_calendar = Calendar(2, 28, 2000)
        test_calendar.write_out()
        test_calendar.advance_day()
        self.assertEqual("Today's Date: Tuesday, February 29th, 2000", test_calendar.date())

    def test_advance_leap_year_to_march(self):
        test_calendar = Calendar(2, 29, 2000)
        test_calendar.write_out()
        test_calendar.advance_day()
        self.assertEqual("Today's Date: Wednesday, March 1st, 2000", test_calendar.date())

    def test_advance_not_leap_year(self):
        test_calendar = Calendar(2, 28, 2001)
        test_calendar.write_out()
        test_calendar.advance_day()
        self.assertEqual("Today's Date: Thursday, March 1st, 2001", test_calendar.date())

if __name__ == '__main__':
    unittest.main()
