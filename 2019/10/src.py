# depths: [int(str(d).strip()) for d in f.readlines()]
import numpy as np
from collections import defaultdict
from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
# import itertools
# import copy

# print(np.arctan2(-.0000000001, -1) * 180 / np.pi)

asteroids = set()
with open("input.txt") as file:
    x = y = 0
    for char in file.read():
        if char == '#':
            asteroids.add((x, y))
            x += 1
        elif char == "\n":
            y += 1
            x = 0
        else:
            x += 1

print(asteroids)


def calc_unit_vector(vector):
    x, y = vector
    if x == 0:
        return 0, y // abs(y)
    if y == 0:
        return x // abs(x), 0

    for divisor in range(min(abs(x), abs(y)), 1, -1):
        if (x % divisor == 0) and (y % divisor == 0):
            return x // divisor, y // divisor

    return vector


def calc_n_visible(monitoring_station: tuple, asteroids: set):
    other_asteroids = asteroids - {monitoring_station}
    unit_vectors = set()
    for asteroid in other_asteroids:
        diff = (monitoring_station[0] - asteroid[0], monitoring_station[1] - asteroid[1])
        unit_vectors.add(calc_unit_vector(diff))
    return len(unit_vectors)


def find_asteroid_with_best_view(asteroids: set):
    n_visible_max = 0
    coords_max = None
    for asteroid in asteroids:
        n_visible = calc_n_visible(asteroid, asteroids)
        if n_visible > n_visible_max:
            n_visible_max = n_visible
            coords_max = asteroid
    return coords_max


laser_coords = find_asteroid_with_best_view(asteroids)
print(laser_coords)

Asteroid = namedtuple("Asteroid", ("coords", "distance", "radians"))
asteroids_by_angle = defaultdict(list)
for asteroid in asteroids - {laser_coords}:
    diff = (asteroid[0] - laser_coords[0], asteroid[1] - laser_coords[1])
    radians = round(np.arctan2(diff[0], diff[1]), 10)  # straight up is +pi, moving clockwise goes down to 0 and then -pi
    a = Asteroid(asteroid, abs(diff[0]) + abs(diff[1]), radians)
    asteroids_by_angle[radians].append(a)

for asteroid_list in asteroids_by_angle.values():
    asteroid_list.sort(key=lambda asteroid: asteroid.distance)

all_angles = sorted(asteroids_by_angle.keys(), reverse=True)

n_vaporized = 1
for angle in all_angles:
    if asteroids_by_angle[angle]:
        asteroid = asteroids_by_angle[angle].pop(0)
        print(n_vaporized, asteroid.coords)
        n_vaporized += 1