#!/usr/bin/python3
import sys
from enum import Enum
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
if __name__ == "__main__":
    COLOR_THRESHOLDS = {
        Color.RED.value: 12,
        Color.GREEN.value: 13,
        Color.BLUE.value: 14
    }
    with open(sys.argv[1], "rt") as input_file:
        possible_games = []
        for line in input_file:
            game_is_possible = True
            game, sets = line.split(":")
            game_id = game.split(" ")[-1]
            drawn_sets = sets.split(";")
            for color_sets in drawn_sets:
                cubes = color_sets.split(",")
                for cube in cubes:
                    for color in Color:
                        if cube.find(color.value) != -1:
                            cubes_number = cube.split(" ")[1]
                            if int(cubes_number) > COLOR_THRESHOLDS[color.value]:
                                game_is_possible = False
                                break
                    if not game_is_possible:
                        break
                if not game_is_possible:
                    break
            if game_is_possible:
                possible_games.append(int(game_id))
        print(sum(possible_games))

