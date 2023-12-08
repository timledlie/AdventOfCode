# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
# from copy import deepcopy
import datetime

active_coords = set()
with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    x = y = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == '#':
                active_coords.add((x, y, 0, 0))


class NeighborFinder():

    def __init__(self):
        self._neighbors = {}

    def get_neighbors(self, coords):
        if coords in self._neighbors:
            return self._neighbors[coords]

        neighbors = set()
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        neighbors.add((coords[0] + x, coords[1] + y, coords[2] + z, coords[3] + w))
        neighbors.remove(coords)
        self._neighbors[coords] = neighbors
        return neighbors


def get_coords_inactive(active_coords):
    some_active_coord = next(iter(active_coords))
    min_coords = [some_active_coord[0], some_active_coord[1], some_active_coord[2], some_active_coord[3]]
    max_coords = [some_active_coord[0], some_active_coord[1], some_active_coord[2], some_active_coord[3]]
    for active_coord in active_coords:
        min_coords[0] = min(min_coords[0], active_coord[0])
        min_coords[1] = min(min_coords[1], active_coord[1])
        min_coords[2] = min(min_coords[2], active_coord[2])
        min_coords[3] = min(min_coords[3], active_coord[3])
        max_coords[0] = max(max_coords[0], active_coord[0])
        max_coords[1] = max(max_coords[1], active_coord[1])
        max_coords[2] = max(max_coords[2], active_coord[2])
        max_coords[3] = max(max_coords[3], active_coord[3])
    all_coords = set()
    for x in range(min_coords[0] - 1, max_coords[0] + 2):
        for y in range(min_coords[1] - 1, max_coords[1] + 2):
            for z in range(min_coords[2] - 1, max_coords[2] + 2):
                for w in range(min_coords[3] - 1, max_coords[3] + 2):
                    all_coords.add((x, y, z, w))
    return all_coords - active_coords


print(len(active_coords), active_coords)
inactive_coords = get_coords_inactive(active_coords)
print(len(inactive_coords), inactive_coords)

print(len(active_coords))
cycles = 6
neighbor_finder = NeighborFinder()
for cycle in range(1, cycles + 1):
    active_coords_next = set()
    for coords in active_coords:
        neighbors = neighbor_finder.get_neighbors(coords)
        if len(neighbors & active_coords) in (2, 3):
            active_coords_next.add(coords)
    for coords in get_coords_inactive(active_coords):
        neighbors = neighbor_finder.get_neighbors(coords)
        if len(neighbors & active_coords) == 3:
            active_coords_next.add(coords)
    active_coords = active_coords_next
    print("After", cycle, "cycles, there are", len(active_coords), "active")
