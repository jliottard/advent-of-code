#!/usr/bin/python3
import sys
from copy import copy

def is_part_number(x:int, y: int, matrice: list) -> bool:
    width, height = len(matrice[y]), len(matrice)
    positions = [
        (x-1,y-1),(x,y-1),(x+1,y-1),
        (x-1,y),        (x+1, y),
        (x-1,y+1),(x,y+1),(x+1,y+1)
    ]
    def in_bounds(x, y) -> bool:
        return 0<=x<width and 0<=y<height
    for pos in positions:
        if in_bounds(pos[0], pos[1]):
            if matrice[pos[1]][pos[0]] != '.' and not matrice[pos[1]][pos[0]].isdigit():
                return True
    return False

def matrice_digits_to_number(digit_x: int, digit_y: int, matrice: list) -> tuple[int, int]:
    # We assume the digits are vertically aligned 
    # return the parsed number and the number of parsed character after the
    # start_digit_x positions
    digits = ""
    start_digit_x = copy(digit_x)
    while 0 <= start_digit_x - 1 and matrice[digit_y][start_digit_x-1].isdigit():
        start_digit_x -= 1
    for x in range(start_digit_x, len(matrice[digit_y])):
        sym = matrice[digit_y][x]
        if not sym.isdigit():
            break
        digits += sym
    n_steps = x - digit_x  
    return int(digits), n_steps

if __name__ == "__main__":
    engine_matrice = []
    with open(sys.argv[1], "rt") as input_file:
        for line in input_file:
            engine_matrice.append(line)
        part_numbers = []
        height = len(engine_matrice)
        for y in range(height):
            row = engine_matrice[y]
            width = len(row)
            x = 0
            while x < width:
                if row[x].isdigit():
                    if is_part_number(x, y, engine_matrice):
                        part_number, steps = matrice_digits_to_number(x, y,
                            engine_matrice)
                        part_numbers.append(part_number)
                        x += steps
                x += 1
        print(part_numbers)
        print(sum(part_numbers))

