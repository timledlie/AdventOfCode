# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# import math
# import json
# import copy
from collections import defaultdict

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    steps = []
    for line in lines:
        parts = line.split(',')
        x_parts = parts[0].split("=")
        y_parts = parts[1].split("=")
        z_parts = parts[2].split("=")
        steps.append((parts[0].split(' ')[0], [int(s) for s in x_parts[1].split("..")], [int(s) for s in y_parts[1].split("..")], [int(s) for s in z_parts[1].split("..")]))

for step in steps:
    print(step)


def dumb_implementation():
    grid = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for step in steps:
        print("Processing step", step)
        bit = 1 if step[0] == 'on' else 0
        if step[1][0] >= -50 and step[1][0] <= 50:
            for x in range(step[1][0], step[1][1] + 1):
                for y in range(step[2][0], step[2][1] + 1):
                    for z in range(step[3][0], step[3][1] + 1):
                        grid[x][y][z] = bit

    on_count = 0
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                if grid[x][y][z]:
                    on_count += 1
    print(on_count)

def get_volume(step):
    vol = (step[1][1] - step[1][0] + 1) * (step[2][1] - step[2][0] + 1) * (step[3][1] - step[3][0] + 1)
    if step[0] == "off":
        vol *= -1
    return vol


def get_overlap_helper(range1, range2):
    return (range1[0] <= range2[1] <= range1[1]) or \
           (range1[0] <= range2[0] <= range1[1]) or \
           ((range2[0] < range1[0]) and (range2[1] > range1[1]))


def get_overlap(step1, step2):
    if get_overlap_helper(step1[1], step2[1]) and \
            get_overlap_helper(step1[2], step2[2]) and \
            get_overlap_helper(step1[3], step2[3]):
        if step1[1][0] <= step2[1][0]:
            min_x = step2[1][0]
        else:
            min_x = step1[1][0]
        if step1[2][0] <= step2[2][0]:
            min_y = step2[2][0]
        else:
            min_y = step1[2][0]
        if step1[3][0] <= step2[3][0]:
            min_z = step2[3][0]
        else:
            min_z = step1[3][0]

        if step1[1][1] >= step2[1][1]:
            max_x = step2[1][1]
        else:
            max_x = step1[1][1]
        if step1[2][1] >= step2[2][1]:
            max_y = step2[2][1]
        else:
            max_y = step1[2][1]
        if step1[3][1] >= step2[3][1]:
            max_z = step2[3][1]
        else:
            max_z = step1[3][1]

        step1_command = step1[0]
        step2_command = step2[0]
        if step1_command == "on" and step2_command == "on":
            overlap_command = "off"
        elif step1_command == "off" and step2_command == "off":
            overlap_command = "on"
        elif step1_command == "on" and step2_command == "off":
            overlap_command = "on"
        elif step1_command == "off" and step2_command == "on":
            overlap_command = "off"

        return (overlap_command, [min_x, max_x], [min_y, max_y], [min_z, max_z])
    else:
        return None


def is_same_region(layer1, layer2):
    return (layer1[1][0] == layer2[1][0]) and (layer1[1][1] == layer2[1][1]) and \
           (layer1[2][0] == layer2[2][0]) and (layer1[2][1] == layer2[2][1]) and \
           (layer1[3][0] == layer2[3][0]) and (layer1[3][1] == layer2[3][1])


def calculate_overlap_adjustment(step_index):
    adjustment = 0
    overlapping_layers = []
    for i in range(step_index - 1, -1, -1):
        overlap = get_overlap(steps[step_index], steps[i])
        if overlap is not None:
            adjustment += get_volume(overlap)
            if (not is_same_region(overlap, steps[step_index])) and \
                (not is_same_region(overlap, steps[i])):
                overlapping_layers.append(overlap)
    return adjustment + overlap_adjustment(overlapping_layers)


def overlap_adjustment(overlapping_layers):
    adjustment = 0
    if len(overlapping_layers) > 1:
        next_overlapping_layers = []
        for i in range(len(overlapping_layers) - 1):
            for j in range(i + 1, len(overlapping_layers)):
                layer = get_overlap(overlapping_layers[i], overlapping_layers[j])
                if layer is not None:
                    adjustment += get_volume(layer)
                    if (not is_same_region(layer, overlapping_layers[i])) and \
                            (not is_same_region(layer, overlapping_layers[j])):
                        next_overlapping_layers.append(layer)
        adjustment += overlap_adjustment(next_overlapping_layers)
    return adjustment


# dumb_implementation()

cuboids = []
for step in steps:
    intersections = []
    for cuboid in cuboids:
        overlap = get_overlap(step, cuboid)
        if overlap is not None:
            intersections.append(overlap)

    for intersection in intersections:
        cuboids.append(intersection)

    if step[0] == "on":
        cuboids.append(step)

n_on = 0
for cuboid in cuboids:
    n_on += get_volume(cuboid)

print(n_on)