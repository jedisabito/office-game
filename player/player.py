class Player:
    def __init__(self, name):
        self.__name = name
        self.__stats = {
            'Knowledge': 0,
            'Diligence': 0,
            'Cooking': 0,
            'Stamina': 0
        }
        self.__location = "Home"

    def move(self, location):
        self.__location = location

    def stat_up(self, stat):
        self.__stats[stat] += 1

    def stat_way_up(self, stat):
        self.__stats[stat] += 3

    def get_stat(self, stat):
        return self.__stats[stat]

    def get_location(self):
        return self.__location
