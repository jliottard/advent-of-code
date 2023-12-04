#!/usr/bin/python3
import sys
if __name__ == "__main__":
    with open(sys.argv[1], "rt") as in_file:
        points = 0
        for line in in_file:
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
            if len(inter):
                points += 2**(len(inter)-1)
        print(points)

