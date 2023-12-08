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

instructions = []
with open("input.txt") as file:
    instructions = [line.strip() for line in file.readlines()]
print(instructions)

ship_position = {'x': 0, 'y': 0}  # north and east are positive
waypoint_relative_position = {'x': 10, 'y': 1}
for instruction in instructions:
    action = instruction[:1]
    value = int(instruction[1:])
    if action == 'N':
        waypoint_relative_position['y'] += value
    elif action == 'S':
        waypoint_relative_position['y'] -= value
    elif action == 'E':
        waypoint_relative_position['x'] += value
    elif action == 'W':
        waypoint_relative_position['x'] -= value
    elif action == 'F':
        ship_position['x'] += waypoint_relative_position['x'] * value
        ship_position['y'] += waypoint_relative_position['y'] * value
    else:
        if action == 'L':
            if value == 90:
                value = 270
            elif value == 270:
                value = 90
        # we're moving right / clockwise
        if value == 90:
            temp = waypoint_relative_position['x']
            waypoint_relative_position['x'] = waypoint_relative_position['y']
            waypoint_relative_position['y'] = -1 * temp
        elif value == 180:
            waypoint_relative_position['x'] = -1 * waypoint_relative_position['x']
            waypoint_relative_position['y'] = -1 * waypoint_relative_position['y']
        elif value == 270:
            temp = waypoint_relative_position['x']
            waypoint_relative_position['x'] = -1 * waypoint_relative_position['y']
            waypoint_relative_position['y'] = temp

print(ship_position)
print(waypoint_relative_position)
print(abs(ship_position['x']) + abs(ship_position['y']))