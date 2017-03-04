import json
from pkg_resources import resource_filename
from player.player import Player
from character.character import Character

player = Player()
player.read_in()


class Dialogue:
    def __init__(self, character, scene):
        path = "../story/characters/" + character + "/dialogue.json"
        with open(resource_filename(self.__module__, path)) as f:
            dialogue_data = json.loads(f.read())
            self.__scene = dialogue_data["scenes"][scene]
        self.read_scene()

    def read_scene(self):
        flags = []
        for line in self.__scene:
            if line["type"] == "narration":
                print line["line"]
                raw_input()
            elif line["type"] == "effect":
                self.effect(line["trigger"], line["effect"], flags)
            else:
                if line["name"] == "MC":
                    name = player.get_name()
                else:
                    name = line["name"].upper()
                if line["type"] == "basic_line":
                    print name + ": " + line["line"]
                    raw_input()
                elif line["type"] == "conditional_line":
                    self.conditional_line(name, line, flags)
                else:
                    flags = self.dialogue_option(line["choices"], flags)

    @staticmethod
    def effect(trigger, effect, flags):
        if trigger == {} or (trigger["type"] == "flag" and trigger["flag"] in flags):
            if effect["type"] == "stat":
                if effect["result"] == "+1":
                    player.stat_up(effect["stat"])
                    print effect["description"]
                    raw_input()
                    print "Your " + effect["stat"].upper() + " has increased."
                elif effect["result"] == "+2":
                    player.stat_way_up(effect["stat"])
                    print effect["description"]
                    raw_input()
                    print "Your " + effect["stat"].upper() + " has greatly increased."
            elif effect["type"] == "character":
                character = Character(effect["character"].lower())
                character.read_in()
                if effect["result"] == "+1":
                    character.friendship_up()
                elif effect["result"] == "+2":
                    character.friendship_way_up()
                print effect["description"] + " (" + effect["result"] + ")"
            raw_input()

    @staticmethod
    def dialogue_option(choices, flags):
        print "What should you say?"
        num_options = len(choices)
        for i in range(num_options):
            choice = choices[i]
            print str(i + 1) + ". " + choice["line"]
        option = raw_input(">: ")
        print ""
        for i in range(num_options):
            if i == int(option) - 1:
                if choices[i]["flag"] != "":
                    flags.append(choices[i]["flag"])
                print choices[i]["description"]
                raw_input()
        return flags

    @staticmethod
    def conditional_line(name, line, flags):
        trigger = line["trigger"]
        if trigger["type"] == "flag" and trigger["flag"] in flags:
            print name + ": " + line["line"]
            raw_input()
