#!/usr/bin/python3
import sys
from collections import defaultdict

def winning_numbers(line: str) -> tuple[int, int]:
    card_id, numbers = line.split(":")
    win_num, your_num = numbers.split("|")
    wins = win_num[1:-1].split(" ")
    try:
        while True:
            wins.remove('')
    except:
        pass
    yours = your_num[1:].split(" ")
    try:
        while True:
            yours.remove('')
    except:
        pass
    wins = set(map(int, wins))
    yours = set(map(int, yours))
    inter = wins.intersection(yours)
    game_id = int(card_id.split(" ")[-1])
    return game_id, len(inter)

if __name__ == "__main__":
    with open(sys.argv[1], "rt") as in_file:
        id_to_cards = defaultdict(int)
        for i, line in enumerate(in_file):
            game_id, won_number_n = winning_numbers(line)
            id_to_cards[i+1] += 1
            for j in range(i+1+1, i+1+won_number_n+1):
                id_to_cards[j] += id_to_cards[i+1]
        print(sum(id_to_cards.values()))

