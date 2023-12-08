# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
# from itertools import combinations
# import copy

orbits = {}
with open("input.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split(')')
        orbits[b] = a

print(orbits)

santa_parents = set()
child = 'SAN'
while orbits[child] != 'COM':
    santa_parents.add(orbits[child])
    child = orbits[child]

child = 'YOU'
first_ancestor = None
while True:
    if orbits[child] in santa_parents:
        first_ancestor = orbits[child]
        break
    child = orbits[child]

print("first ancestor:", first_ancestor)


def distance_to_object(start_object, target_object):
    if orbits[start_object] == target_object:
        return 0
    return 1 + distance_to_object(orbits[start_object], target_object)


print(distance_to_object('SAN', first_ancestor) + distance_to_object('YOU', first_ancestor))