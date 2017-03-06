import unittest
import json
from pkg_resources import resource_filename
from player.player import Player


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_player = Player()
        cls.test_player.write_out()
        with open(resource_filename(cls.__module__, '../game_data/player.json'), 'r') as f:
            cls.player_data = json.loads(f.read())

    def read_in(self):
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            return json.loads(f.read())

    def test_write_name(self):
        self.assertEqual(self.player_data['name'], self.test_player.get_name())

    def test_read_name(self):
        with open(resource_filename(self.__module__, '../story/player/player.json'), 'r') as f:
            story_player_data = json.loads(f.read())
            self.assertEqual(story_player_data["name"], self.player_data["name"])

    def test_stats_up(self):
        self.test_player.stat_up("Knowledge")
        self.player_data = self.read_in()
        self.assertEqual(self.player_data["stats"]["Knowledge"], 1)

    def test_stats_way_up(self):
        self.test_player.stat_way_up("Stamina")
        self.player_data = self.read_in()
        self.assertEqual(self.player_data["stats"]["Stamina"], 2)
