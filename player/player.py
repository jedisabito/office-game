import json
from pkg_resources import resource_filename


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
        self.update()

    def update(self):
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'w+') as f:
            f.write(json.dumps({
                'name': self.__name,
                'stats': self.__stats,
                'location': self.__location
            }))

    def move(self, location):
        self.__location = location
        self.update()

    def stat_up(self, stat):
        self.__stats[stat] += 1
        self.update()

    def stat_way_up(self, stat):
        self.__stats[stat] += 3
        self.update()

    def get_stat(self, stat):
        return self.__stats[stat]

    def get_location(self):
        return self.__location

    def get_name(self):
        return self.__name


