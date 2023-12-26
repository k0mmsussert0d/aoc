import fileinput
import re


if __name__ == "__main__":
    res = 0
    for card in fileinput.input():
        card = re.split(":|\|", card)
        wins = [int(x) for x in re.split("\s+", card[1].strip())]
        hand = [int(x) for x in re.split("\s+", card[2].strip())]
        common = set(wins) & set(hand)
        if common:
            res += 2 ** (len(common) - 1)
    
    print(res)
