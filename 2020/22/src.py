# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# import math
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
import copy

with open("input.txt") as file:
    file_text = file.read()

p1, p2 = file_text.split("\n\n")
p1 = [int(card) for card in p1.strip().split()[2:]]
p2 = [int(card) for card in p2.strip().split()[2:]]
print(p1)
print(p2)


def remember_hands(all_hands, p1, p2):
    all_hands.add((tuple(p1), tuple(p2)))


def been_here_before(all_hands, p1, p2):
    return (tuple(p1), tuple(p2)) in all_hands


def combat(p1, p2):
    all_hands = set()
    while (len(p1) > 0) and (len(p2) > 0):
        if (been_here_before(all_hands, p1, p2)):
            return 'p1'
        remember_hands(all_hands, p1, p2)

        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        if (p1_card <= len(p1)) and (p2_card <= len(p2)):
            p1_copy = copy.copy(p1)
            p2_copy = copy.copy(p2)
            winner = combat(p1_copy[:p1_card], p2_copy[:p2_card])
        else:
            winner = 'p1' if p1_card > p2_card else 'p2'
        if winner == 'p1':
            p1.extend([p1_card, p2_card])
        else:
            p2.extend([p2_card, p1_card])

    return 'p1' if len(p1) else 'p2'


winner = p1 if combat(p1, p2) == 'p1' else p2
multiplier = len(winner)
score = 0
for card in winner:
    score += multiplier * card
    multiplier -= 1
print(score)