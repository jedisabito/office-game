import json
from pkg_resources import resource_filename


class Character:
    def __init__(self, name):
        path = '../story/characters/' + name + '/info.json'
        with open(resource_filename(self.__module__, path), 'r') as f:
            character_data = json.loads(f.read())
            self.__name = character_data["name"]
            self.__outfits = character_data["outfits"]
            self.__locations = character_data["locations"]
            self.__friendship = character_data["friendship"]
        self.path = '../game_data/characters/' + name + '.json'

    def read_in(self):
        with open(resource_filename(self.__module__, self.path), 'r') as f:
            character_data = json.loads(f.read())
            self.__name = character_data["name"]
            self.__outfits = character_data["outfits"]
            self.__locations = character_data["locations"]
            self.__friendship = character_data["friendship"]

    def write_out(self):
        with open(resource_filename(self.__module__, self.path), 'w+') as f:
            f.write(json.dumps({
                'name': self.__name,
                'outfits': self.__outfits,
                'locations': self.__locations,
                'friendship': self.__friendship
            }))

    def friendship_up(self):
        self.read_in()
        self.__friendship += 1
        self.write_out()

    def friendship_way_up(self):
        self.read_in()
        self.__friendship += 2
        self.write_out()
