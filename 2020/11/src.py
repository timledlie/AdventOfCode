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
from copy import deepcopy

seats = []
with open("input.txt") as file:
    for line in file.readlines():
        row = ['.'] + [c for c in line.strip()] + ['.']
        seats.append(row)

n_cols = len(seats[0])
seats.append(['.'] * n_cols)
seats = [['.'] * n_cols] + seats
n_rows = len(seats)

def pretty_print(seats):
    for row in seats[1:-1]:
        print(''.join(row[1:-1]))
    print()

pretty_print(seats)

def count_occupied_nearby(row, col, seats):
    n_occupied = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if not ((r == row) and (c == col)):
                if seats[r][c] == '#':
                    n_occupied += 1
    return n_occupied

def count_occupied_in_sight(row, col, seats):
    n_occupied = 0
    # up
    for r in range(row - 1, 0, -1):
        seat = seats[r][col]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    # down
    for r in range(row + 1, n_rows, 1):
        seat = seats[r][col]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    # left
    for c in range(col - 1, 0, -1):
        seat = seats[row][c]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    # right
    for c in range(col + 1, n_cols, 1):
        seat = seats[row][c]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    # down-right
    for r, c in zip(range(row + 1, n_rows), range(col + 1, n_cols)):
        seat = seats[r][c]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    for r, c in zip(range(row + 1, n_rows), range(col - 1, 0, -1)):
        seat = seats[r][c]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    for r, c in zip(range(row - 1, 0, -1), range(col + 1, n_cols)):
        seat = seats[r][c]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    for r, c in zip(range(row - 1, 0, -1), range(col - 1, 0, -1)):
        seat = seats[r][c]
        if seat == '#':
            n_occupied += 1
            break
        if seat == 'L':
            break
    return n_occupied


n_changes = 1
while n_changes:
    n_changes = 0
    seats_next = deepcopy(seats)
    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            seat = seats[row][col]
            if seat != '.':
                n_occupied = count_occupied_in_sight(row, col, seats)
                if seat == 'L' and n_occupied == 0:
                    seats_next[row][col] = '#'
                    n_changes += 1
                elif seat == '#' and n_occupied >= 5:
                    seats_next[row][col] = 'L'
                    n_changes += 1
    seats = seats_next
    pretty_print(seats)

n_occupied = 0
for row in range(1, n_rows - 1):
    for col in range(1, n_cols - 1):
        if seats[row][col] == '#':
            n_occupied += 1
print(n_occupied)
