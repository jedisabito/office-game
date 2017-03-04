import unittest
import json
from pkg_resources import resource_filename
from player.player import Player


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_player = Player("Test")
        cls.test_player.write_out()

    def test_update(self):
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            self.assertEqual(player_data['name'], self.test_player.get_name())

    def test_stats_up(self):
        self.test_player.stat_up("Knowledge")
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            self.assertEqual(player_data["stats"]["Knowledge"], 1)

    def test_stats_way_up(self):
        self.test_player.stat_way_up("Stamina")
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            self.assertEqual(player_data["stats"]["Stamina"], 2)
