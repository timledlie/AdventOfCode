# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
from collections import defaultdict
# import math
# import json

scanners = []
beacons = []
universe = set()  # set of all beacons from scanner 0's point of view (coordinate system)
# transformations = {0: "(x,y,z)"}  # map of scanner ID to transformation to scanner 0's coordinate system
scanners_inside_universe = [0]
scanners_outside_universe = []
distance_to_universe_origin = {0: (0, 0, 0)}
with open("input.txt") as file:
    i = 0
    for line in file.readlines():
        if line == "\n":
            scanners.append(beacons)
            if i != 0:
                scanners_outside_universe.append(i)
            i += 1
            beacons = []
        elif line[0:3] == "---":
            continue
        else:
            coords = line.strip().split(',')
            beacons.append((int(coords[0]), int(coords[1]), int(coords[2])))
    scanners.append(beacons)
    scanners_outside_universe.append(i)

# initialize universe with all beacons from scanner 0
for beacon in scanners[0]:
    universe.add(beacon)


def make_permutations(scanner):
    coords = [[] for n in range(24)]
    for x, y, z in scanner:
        coords[0].append((x,y,z))
        coords[1].append((y,-1*x,z))
        coords[2].append((-1*x,-1*y,z))
        coords[3].append((-1*y,x,z))
        coords[4].append((x,z,-1*y))
        coords[5].append((z,-1*x,-1*y))
        coords[6].append((-1*x,-1*z,-1*y))
        coords[7].append((-1*z,x,-1*y))
        coords[8].append((x,-1*z,y))
        coords[9].append((-1*z,-1*x,y))
        coords[10].append((-1*x,z,y))
        coords[11].append((z,x,y))
        coords[12].append((y,z,x))
        coords[13].append((z,-1*y,x))
        coords[14].append((-1*y,-1*z,x))
        coords[15].append((-1*z,y,x))
        coords[16].append((x,-1*y,-1*z))
        coords[17].append((-1*y,-1*x,-1*z))
        coords[18].append((-1*x,y,-1*z))
        coords[19].append((y,x,-1*z))
        coords[20].append((y,-1*z,-1*x))
        coords[21].append((-1*z,-1*y,-1*x))
        coords[22].append((-1*y,z,-1*x))
        coords[23].append((z,y,-1*x))
    return coords


def make_distances(coord_list):
    distances_list = set()
    for i in range(len(coord_list)):
        for j in range(len(coord_list)):
            if i != j:
                distances_list.add((coord_list[i][0] - coord_list[j][0], coord_list[i][1] - coord_list[j][1], coord_list[i][2] - coord_list[j][2]))
    return distances_list


def make_distances_map(coord_list):
    distances_map = {}
    for i in range(len(coord_list)):
        for j in range(len(coord_list)):
            if i != j:
                distances_map[(coord_list[i][0] - coord_list[j][0], coord_list[i][1] - coord_list[j][1], coord_list[i][2] - coord_list[j][2])] = (coord_list[i], coord_list[j])
    return distances_map


# initialize all scanner's beacon coordinates permutations and their distances and distance maps
permutations = []
distances = []
distances_maps = []
for scanner in scanners:
    this_scanner_permutations = make_permutations(scanner)
    permutations.append(this_scanner_permutations)
    this_scanner_distances = []
    this_scanner_distances_maps = []
    for permutation in this_scanner_permutations:
        this_scanner_distances.append(make_distances(permutation))
        this_scanner_distances_maps.append(make_distances_map(permutation))
    distances.append(this_scanner_distances)
    distances_maps.append(this_scanner_distances_maps)

while scanners_outside_universe:
    for scanner_id_inside in scanners_inside_universe:
        for scanner_id_outside in scanners_outside_universe:
            max_matches = 0
            max_matches_index = -1
            for i in range(len(distances[scanner_id_outside])):
                matching_distances = distances[scanner_id_outside][i].intersection(distances[scanner_id_inside][0])
                print("scanner_id_inside", scanner_id_inside, "scanner_id_outside", scanner_id_outside, "permutation", i, "matches", len(matching_distances), "distances")
                if len(matching_distances) > max_matches:
                    max_matches = len(matching_distances)
                    max_matches_index = i
            if max_matches >= 132:
                distances_map = distances_maps[scanner_id_outside][max_matches_index]
                distances_map_keys = distances_map.keys()
                for origin_distance, (origin_beacon1, origin_beacon2) in distances_maps[scanner_id_inside][0].items():
                    if origin_distance in distances_map_keys:
                        scanner_beacon = distances_map[origin_distance][0]
                        scanner_to_scanner_shift = (origin_beacon1[0] - scanner_beacon[0], origin_beacon1[1] - scanner_beacon[1], origin_beacon1[2] - scanner_beacon[2])
                        distance_inside = distance_to_universe_origin[scanner_id_inside]
                        distance_to_universe_origin[scanner_id_outside] = (distance_inside[0] + scanner_to_scanner_shift[0], distance_inside[1] + scanner_to_scanner_shift[1], distance_inside[2] + scanner_to_scanner_shift[2])
                        scanner_to_origin_shift = distance_to_universe_origin[scanner_id_outside]
                        print("Shift from", scanner_id_outside, "to origin is ", scanner_to_origin_shift)
                        for beacon in permutations[scanner_id_outside][max_matches_index]:
                            universe.add((scanner_to_origin_shift[0] + beacon[0], scanner_to_origin_shift[1] + beacon[1], scanner_to_origin_shift[2] + beacon[2]))
                        break
                distances[scanner_id_outside][0] = distances[scanner_id_outside][max_matches_index]
                distances_maps[scanner_id_outside][0] = distances_maps[scanner_id_outside][max_matches_index]
                scanners_inside_universe.append(scanner_id_outside)
                scanners_outside_universe.remove(scanner_id_outside)
                break

print(len(universe))
print(distance_to_universe_origin)
largest_manhattan_distance = 0
for a in distance_to_universe_origin.values():
    for b in distance_to_universe_origin.values():
        manhattan_distance = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        largest_manhattan_distance = max(manhattan_distance, largest_manhattan_distance)
print(largest_manhattan_distance)