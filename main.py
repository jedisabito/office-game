from calendar.calendar import Calendar
from player.player import Player
from time.time import Time
from activity.activity import Activity

game_calendar = Calendar(1, 0, 2000)
end_date = Calendar(1, 3, 2000)
game_time = Time()
main_character = Player("Phil")

while game_calendar.date() != end_date.date():
    game_calendar.advance_day()
    print game_calendar.date()
    Activity()

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

