#!/usr/bin/python3
import sys
from enum import Enum
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
if __name__ == "__main__":
    with open(sys.argv[1], "rt") as input_file:
        powers = 0
        for line in input_file:
            game, sets = line.split(":")
            game_id = game.split(" ")[-1]
            drawn_sets = sets.split(";")
            minimum_cubes = {c: 0 for c in [c.value for c in Color]}
            for color_sets in drawn_sets:
                cubes = color_sets.split(",")
                for cube in cubes:
                    for color in Color:
                        if cube.find(color.value) != -1:
                            cubes_number = int(cube.split(" ")[1])
                            if cubes_number > minimum_cubes[color.value]:
                                minimum_cubes[color.value] = cubes_number
            power = 1
            for minimum in minimum_cubes.values():
                power *= minimum
            powers += power
        print(powers)

