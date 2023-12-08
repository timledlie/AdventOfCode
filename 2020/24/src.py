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
    lines = [list(line.strip()) for line in file.readlines()]

blacks = set()
min_x, min_y, max_x, max_y = 0, 0, 0, 0
for line in lines:
    x, y = 0, 0
    while line:
        direction = line.pop(0)
        if direction in ('n', 's'):
            direction += line.pop(0)

        if direction == 'e':
            x += 2
        elif direction == 'se':
            x += 1
            y -= 1
        elif direction == 'sw':
            x -= 1
            y -= 1
        elif direction == 'w':
            x -= 2
        elif direction == 'nw':
            x -= 1
            y += 1
        elif direction == 'ne':
            x += 1
            y += 1
        else:
            exit("poop")
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    if (x, y) in blacks:
        blacks.remove((x, y))
    else:
        blacks.add((x, y))

print("Day 0:", len(blacks))


def get_neighbor_black_count(x, y, blacks):
    n_blacks = 0
    for x_diff, y_diff in ((2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)):
        if (x + x_diff, y + y_diff) in blacks:
            n_blacks += 1
    return n_blacks


for day in range(1, 101):
    blacks_next = copy.copy(blacks)
    min_x_next, min_y_next, max_x_next, max_y_next = min_x, min_y, max_x, max_y
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x % 2) != (y % 2):
                continue
            neighbor_black_count = get_neighbor_black_count(x, y, blacks)
            if (x, y) in blacks:
                if neighbor_black_count not in (1, 2):
                    blacks_next.remove((x, y))
            else:
                if neighbor_black_count == 2:
                    blacks_next.add((x, y))
                    min_x_next = min(min_x_next, x)
                    min_y_next = min(min_y_next, y)
                    max_x_next = max(max_x_next, x)
                    max_y_next = max(max_y_next, y)
    blacks = blacks_next
    min_x = min_x_next
    min_y = min_y_next
    max_x = max_x_next
    max_y = max_y_next
    print("Day", day, ":", len(blacks))