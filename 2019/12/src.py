# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
import itertools
# import copy

class Moon:
    def __init__(self, position: list):
        self.position = position
        self.velocity = [0, 0, 0]

    def apply_gravity(self, other_moon):
        for axis in range(3):
            if self.position[axis] < other_moon.position[axis]:
                self.velocity[axis] += 1
            elif self.position[axis] > other_moon.position[axis]:
                self.velocity[axis] -= 1

    def apply_velocity(self):
        for axis in range(3):
            self.position[axis] += self.velocity[axis]

    def total_energy(self):
        potential_energy = kinetic_energy = 0
        for pos in self.position:
            potential_energy += abs(pos)
        for vel in self.velocity:
            kinetic_energy += abs(vel)
        return potential_energy * kinetic_energy


def system_enery(moons):
    total = 0
    for moon in moons:
        total += moon.total_energy()
    return total


def averages(moons):
    positions = [0, 0, 0]
    velocities = [0, 0, 0]
    for moon in moons:
        for axis in range(3):
            positions[axis] += moon.position[axis]
            velocities[axis] += moon.velocity[axis]
    return [[positions[0] / 4, positions[1] / 4, positions[2] / 4],
            [velocities[0] / 4, velocities[1] / 4, velocities[2] / 4]]


def print_moons(moons):
    for moon in moons:
        print(f'{moon.position[0]:>4}', f'{moon.position[1]:>4}', f'{moon.position[2]:>4}', sep=', ', end=' ')
        print(f'{moon.velocity[0]:>4}', f'{moon.velocity[1]:>4}', f'{moon.velocity[2]:>4}', sep=', ', end=' || ')
    print()


moons = []
with open("input.txt") as file:
    for line in file.readlines():
        parts = line.split('=')
        x = int(parts[1].split(',')[0])
        y = int(parts[2].split(',')[0])
        z = int(parts[3].split('>')[0])
        moons.append(Moon([x, y, z]))

for step in range(30000000):
    se = system_enery(moons)
    if step != 0 and se == 0:
        print("after", f'{step:>3}', "steps ", end='')
        print(f'{str(averages(moons)):>5}', end=': ')
        print(f'{se:>5}', end=': ')
        print_moons(moons)

    for moon_a, moon_b in itertools.product(moons, repeat=2):
        if moon_a != moon_b:
            moon_a.apply_gravity(moon_b)

    for moon in moons:
        moon.apply_velocity()

print(system_enery(moons))