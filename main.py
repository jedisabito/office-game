from gamecalendar.calendar import Calendar
from player.player import Player
from gametime.time import Time
from activity.activity import Activity
from weather.weather import Weather
from utils.utils import Utilities

print '''Welcome!
1. New game
2. Load game
'''
choice = raw_input(">: ")
Utilities(choice)

game_calendar = Calendar()
game_time = Time()
game_weather = Weather()

while game_calendar.its_not_the_end():
    print game_calendar.date()
    print game_weather.get_weather(game_calendar.raw_date())
    print game_time.get_time()
    raw_input()
    game_time.advance_time()
    if game_time.get_raw_time() == 0:
        game_calendar.advance_day()

print "Time stopped."


'''
day by day loop:
    advance calendar
    morning (time 0)
       breakfast
    work (or activities on weekends) (time 1)
       elevator
       getting coffee
       office
       (meeting)
       lunch (time 2)
       do work
       water cooler break (time 3)
       take the elevator back down
    back home
       dinner (time 4)
       activities (time 5)

activities:
    library
    groceries
    video games
    call someone and hang out
    hit the gym
    do more work
    read
'''

