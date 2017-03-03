from library.library import Library
from gym.gym import Gym
from groceries.groceries import Groceries
from call.call import Call
from book.book import Book
from videogames.videogames import VideoGames


class Activity:
    def __init__(self):
        print '''Would you like to:
        1. Go somewhere
        2. Call someone
        3. Read a book
        4. Play video games
        '''
        choice = raw_input(">: ")
        if choice == "1":
            print '''Where would you like to go?
            1. Library
            2. Gym
            3. Supermarket
            '''
            choice = raw_input(">: ")
            if choice == "1":
                Library()
            elif choice == "2":
                Gym()
            else:
                Groceries()
        elif choice == "2":
            Call()
        elif choice == "3":
            Book()
        else:
            VideoGames()
