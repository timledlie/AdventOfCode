start_replacement = "|"
row_delta, col_delta = 1, 0

with open("input.txt") as file:
    network = [list(line.strip()) for line in file.readlines()]


def pad_circumference(network):
    network_paddded = [["."] * (len(network[0]) + 2)]
    for row in network:
        network_paddded.append(["."] + row + ["."])
    network_paddded.append(["."] * (len(network[0]) + 2))
    return network_paddded


def stretch(network):
    network_stretched = []
    for row in range(len(network)):
        this_row, next_row = [], []
        for col in range(len(network[0])):
            pipe_type = network[row][col]
            this_row.append(pipe_type)
            if pipe_type == "|":
                this_row.append(".")
                next_row.extend(["|", "."])
            elif pipe_type == "-":
                this_row.append("-")
                next_row.extend([".", "."])
            elif pipe_type == "L":
                this_row.append("-")
                next_row.extend([".", "."])
            elif pipe_type == "J":
                this_row.append(".")
                next_row.extend([".", "."])
            elif pipe_type == "7":
                this_row.append(".")
                next_row.extend(["|", "."])
            elif pipe_type == "F":
                this_row.append("-")
                next_row.extend(["|", "."])
            else:
                this_row.append(".")
                next_row.extend([".", "."])
        network_stretched.extend([this_row, next_row])
    return network_stretched


def find_start_location(network):
    for row in range(len(network)):
        for col in range(len(network[0])):
            if network[row][col] == "S":
                return row, col


def walk_network(network, prev_location, cur_location):
    pipe_type = network[cur_location[0]][cur_location[1]]
    if pipe_type == "|":
        if prev_location[0] < cur_location[0]:
            return cur_location[0] + 1, cur_location[1]
        else:
            return cur_location[0] - 1, cur_location[1]
    elif pipe_type == "-":
        if prev_location[1] < cur_location[1]:
            return cur_location[0], cur_location[1] + 1
        else:
            return cur_location[0], cur_location[1] - 1
    elif pipe_type == "L":
        if prev_location[0] < cur_location[0]:
            return cur_location[0], cur_location[1] + 1
        else:
            return cur_location[0] - 1, cur_location[1]
    elif pipe_type == "J":
        if prev_location[0] < cur_location[0]:
            return cur_location[0], cur_location[1] - 1
        else:
            return cur_location[0] - 1, cur_location[1]
    elif pipe_type == "7":
        if prev_location[0] > cur_location[0]:
            return cur_location[0], cur_location[1] - 1
        else:
            return cur_location[0] + 1, cur_location[1]
    elif pipe_type == "F":
        if prev_location[0] > cur_location[0]:
            return cur_location[0], cur_location[1] + 1
        else:
            return cur_location[0] + 1, cur_location[1]


# this process could be more efficient
def outside_locations_step(network, outside_locations, path_locations):
    outside_locations_next = set()
    for location in outside_locations:
        outside_locations_next.add(location)
        for row in range(location[0] - 1, location[0] + 2):
            for col in range(location[1] - 1, location[1] + 2):
                if (0 <= row < len(network)) and (0 <= col < len(network[0])):
                    if (row, col) not in path_locations:
                        outside_locations_next.add((row, col))
    return outside_locations_next


start_location_orig = find_start_location(network)
network[start_location_orig[0]][start_location_orig[1]] = start_replacement

network = stretch(pad_circumference(network))
start_location = (start_location_orig[0] + 1) * 2, (start_location_orig[1] + 1) * 2

prev_location = start_location
cur_location = start_location[0] + row_delta, start_location[1] + col_delta
path_locations = {start_location, cur_location}

while True:
    next_location = walk_network(network, prev_location, cur_location)

    prev_location = cur_location
    cur_location = next_location

    path_locations.add(cur_location)

    if cur_location == start_location:
        break

outside_locations = {(0, 0)}

while True:
    outside_locations_next = outside_locations_step(network, outside_locations, path_locations)
    if outside_locations == outside_locations_next:
        break
    outside_locations = outside_locations_next

all_locations = set()
for row in range(len(network)):
    for col in range(len(network[0])):
        all_locations.add((row, col))

inside_locations = all_locations - outside_locations - path_locations
actual_inside_locations = set()
for location in inside_locations:
    if (location[0] % 2 == 0) and (location[1] % 2 == 0):
        actual_inside_locations.add(location)
print(len(actual_inside_locations))
