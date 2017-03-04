import json
from pkg_resources import resource_filename


class Player:
    def __init__(self, name=None):
        self.__name = name
        self.__stats = {}
        with open(resource_filename(self.__module__,'../story/player/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            for stat in player_data["stats"]:
                self.__stats[stat] = 0
        self.__location = "Home"

    def read_in(self):
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            self.__name = player_data['name']
            self.__stats = player_data['stats']
            self.__location = player_data['location']

    def write_out(self):
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'w+') as f:
            f.write(json.dumps({
                'name': self.__name,
                'stats': self.__stats,
                'location': self.__location
            }))

    def move(self, location):
        self.read_in()
        self.__location = location
        self.write_out()

    def stat_up(self, stat):
        self.read_in()
        self.__stats[stat] += 1
        self.write_out()

    def stat_way_up(self, stat):
        self.read_in()
        self.__stats[stat] += 2
        self.write_out()

    def get_stat(self, stat):
        self.read_in()
        return self.__stats[stat]

    def get_location(self):
        self.read_in()
        return self.__location

    def get_name(self):
        self.read_in()
        return self.__name


