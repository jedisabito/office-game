import unittest
import json
from pkg_resources import resource_filename
from player.player import Player


class TestPlayer(unittest.TestCase):

    def test_update(self):
        test_player = Player("Test")
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            self.assertEqual(player_data['name'], test_player.get_name())

    def test_stats_up(self):
        test_player = Player("Test")
        test_player.stat_up("Knowledge")
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            self.assertEqual(player_data["stats"]["Knowledge"], 1)

    def test_stats_way_up(self):
        test_player = Player("Test")
        test_player.stat_way_up("Stamina")
        with open(resource_filename(self.__module__, '../game_data/player.json'), 'r') as f:
            player_data = json.loads(f.read())
            self.assertEqual(player_data["stats"]["Stamina"], 3)
