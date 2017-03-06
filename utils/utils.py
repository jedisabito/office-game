import json
from character.character import Character
from player.player import Player
from gamecalendar.calendar import Calendar
from gametime.time import Time
from pkg_resources import resource_filename


class Utilities:
    def __init__(self, choice):
        if choice == "1":
            self.new_game()

    def new_game(self):
        self.instantiate_characters()
        self.instantiate_player()
        self.instantiate_calendar()
        self.instantiate_time()

    def instantiate_characters(self):
        with open(resource_filename(self.__module__, '../story/characters/characters.json'), 'r') as f:
            characters_data = json.loads(f.read())
            for character in characters_data["list"]:
                Character(character).write_out()

    @staticmethod
    def instantiate_player():
        new_player = Player()
        new_player.write_out()

    @staticmethod
    def instantiate_calendar():
        new_calendar = Calendar()
        new_calendar.write_out()

    @staticmethod
    def instantiate_time():
        new_time = Time()
        new_time.write_out()