from gamecalendar.gamecalendar import Calendar
from player.player import Player
from gametime.time import Time
from activity.activity import Activity
from weather.weather import Weather

game_calendar = Calendar()
game_time = Time()
game_weather = Weather()
main_character = Player("Phil")

while game_calendar.its_not_the_end():
    print game_calendar.date()
    print "Weather: " + game_weather.get_weather(game_calendar.raw_date())
    Activity()
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
       take the elevator back home
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

