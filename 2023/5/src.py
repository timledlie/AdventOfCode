from collections import namedtuple

CategoryMap = namedtuple('CategoryMap', ['source_to_destination_maps'])
SourceToDestinationMap = namedtuple(
    'SourceToDestinationMap',
    ['source_start', 'source_end', 'destination_start', 'destination_end', 'delta']
)
big_int = 2855283282000

with open("input.txt") as file:
    input_string = file.read()

parts = input_string.strip().split("\n\n")
seeds_data = [int(seed) for seed in parts[0][7:].split()]


def convert_map_lines_to_map(map_string):
    map_lines = map_string.split(":\n")[1].split("\n")
    source_to_destination_maps = []
    max_seed = 0
    for map_line in map_lines:
        map_line_parts = map_line.split()
        destination_start = int(map_line_parts[0])
        source_start = int(map_line_parts[1])
        delta = int(map_line_parts[2])

        source_end = source_start + delta - 1
        destination_end = destination_start + delta - 1

        source_to_destination_maps.append(SourceToDestinationMap(
            source_start,
            source_end,
            destination_start,
            destination_end,
            destination_start - source_start
        ))
        max_seed = max(max_seed, source_end, destination_end)

    return max_seed, CategoryMap(source_to_destination_maps)


def map_source_to_destination(source, category_map):
    for sd_map in category_map.source_to_destination_maps:
        if sd_map.source_start <= source <= sd_map.source_end:
            return sd_map.destination_start + source - sd_map.source_start
    return source


def map_seed_to_location(seed):
    source = seed
    for category_map in category_maps:
        source = map_source_to_destination(source, category_map)
    return source


def is_valid_seed(seed, valid_seed_ranges):
    for seed_range in valid_seed_ranges:
        if seed_range[0] <= seed <= seed_range[1]:
            return True
    return False


def compose_category_maps(cm_a, cm_b):
    sd_maps_composed = []
    for a_sd_map in cm_a.source_to_destination_maps:
        for b_sd_map in cm_b.source_to_destination_maps:
            new_delta = a_sd_map.delta + b_sd_map.delta
            if (a_sd_map.destination_start <= b_sd_map.source_start) and (a_sd_map.destination_end >= b_sd_map.source_end):
                # destination fully covers source
                sd_maps_composed.append(SourceToDestinationMap(b_sd_map.source_start - a_sd_map.delta, b_sd_map.source_end - a_sd_map.delta, b_sd_map.source_start - a_sd_map.delta + new_delta, b_sd_map.source_end - a_sd_map.delta + new_delta, new_delta))
            elif (a_sd_map.destination_start >= b_sd_map.source_start) and (a_sd_map.destination_end <= b_sd_map.source_end):
                # source fully covers destination
                sd_maps_composed.append(SourceToDestinationMap(a_sd_map.source_start, a_sd_map.source_end, a_sd_map.source_start + new_delta, a_sd_map.source_end + new_delta, new_delta))
            elif (a_sd_map.destination_start >= b_sd_map.source_start) and (a_sd_map.destination_start <= b_sd_map.source_end) and (a_sd_map.destination_end > b_sd_map.source_end):
                # partial overlap
                sd_maps_composed.append(SourceToDestinationMap(a_sd_map.source_start, b_sd_map.source_end - a_sd_map.delta, a_sd_map.source_start + new_delta, b_sd_map.source_end - a_sd_map.delta + new_delta, new_delta))
            elif (a_sd_map.destination_end >= b_sd_map.source_start) and (a_sd_map.destination_end <= b_sd_map.source_end) and (a_sd_map.destination_end < b_sd_map.source_end):
                # partial overlap
                sd_maps_composed.append(SourceToDestinationMap(b_sd_map.source_start - a_sd_map.delta, a_sd_map.source_end, b_sd_map.source_start - a_sd_map.delta + new_delta, a_sd_map.source_end + new_delta, new_delta))
    return CategoryMap(sd_maps_composed)


steps = 7
overall_max_seed = 0
category_maps = []
for i in range(1, steps + 1):
    max_seed, category_map = convert_map_lines_to_map(parts[i])
    overall_max_seed = max(overall_max_seed, max_seed)
    category_maps.append(category_map)

padded_category_maps = []
for category_map in category_maps:
    min_start = big_int
    max_end = 0
    for sd_map in category_map.source_to_destination_maps:
        min_start = min(min_start, sd_map.source_start, sd_map.destination_start)
        max_end = max(max_end, sd_map.source_end, sd_map.destination_end)
    additional_sd_maps = []
    if min_start > 0:
        additional_sd_maps.append(SourceToDestinationMap(0, min_start - 1, 0, min_start - 1, 0))
    if max_end < overall_max_seed:
        additional_sd_maps.append(SourceToDestinationMap(max_end + 1, overall_max_seed, max_end + 1, overall_max_seed, 0))
    padded_category_maps.append(CategoryMap(category_map.source_to_destination_maps + additional_sd_maps))

category_maps = padded_category_maps

composed_cm = compose_category_maps(category_maps[5], category_maps[6])
for i in range(4, -1, -1):
    composed_cm = compose_category_maps(category_maps[i], composed_cm)

valid_seed_ranges = []
for i in range(0, len(seeds_data), 2):
    valid_seed_ranges.append((seeds_data[i], seeds_data[i] + seeds_data[i+1] - 1))

print(valid_seed_ranges)
min_location = big_int
for sd_map in composed_cm.source_to_destination_maps:
    for boundary in (sd_map.source_start, sd_map.source_end):
        if is_valid_seed(boundary, valid_seed_ranges):
            min_location = min(min_location, map_seed_to_location(boundary))

print(min_location)
