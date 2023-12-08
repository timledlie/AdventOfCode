# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# import math
# import json
# import copy
# import random
import copy

grid = []
with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        grid.append(list(line))
x_dim = len(grid)
y_dim = len(grid[0])

for line in grid:
    print(line)
print()


def advance_one_step():
    global grid
    n_changes = 0

    grid_next = copy.deepcopy(grid)
    for x in range(x_dim):
        for y in range(y_dim):
            if grid[x][y] == '>':
                if y == (y_dim - 1):
                    if grid[x][0] == '.':
                        grid_next[x][y] = '.'
                        grid_next[x][0] = '>'
                        n_changes += 1
                elif grid[x][y+1] == '.':
                    grid_next[x][y] = '.'
                    grid_next[x][y+1] = '>'
                    n_changes += 1
    grid = grid_next
    grid_next = copy.deepcopy(grid)

    for x in range(x_dim):
        for y in range(y_dim):
            if grid[x][y] == 'v':
                if x == (x_dim - 1):
                    if grid[0][y] == '.':
                        grid_next[x][y] = '.'
                        grid_next[0][y] = 'v'
                        n_changes += 1
                elif grid[x+1][y] == '.':
                    grid_next[x][y] = '.'
                    grid_next[x+1][y] = 'v'
                    n_changes += 1
    grid = grid_next
    return n_changes

n_changes = 1
n_steps = 0
# for i in range(1):
while n_changes:
    n_changes = advance_one_step()
    n_steps += 1
    print(n_steps, n_changes)


for line in grid:
    print(line)
print(n_steps)