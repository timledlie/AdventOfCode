path_a_row_delta, path_a_col_delta = -1, 0
path_b_row_delta, path_b_col_delta = 1, 0

with open("input.txt") as file:
    network = [list(line.strip()) for line in file.readlines()]


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


start_location = find_start_location(network)

prev_location_a = start_location
prev_location_b = start_location
cur_location_a = start_location[0] + path_a_row_delta, start_location[1] + path_a_col_delta
cur_location_b = start_location[0] + path_b_row_delta, start_location[1] + path_b_col_delta
path_a, path_b = {cur_location_a}, {cur_location_b}

while True:
    next_location_a = walk_network(network, prev_location_a, cur_location_a)
    next_location_b = walk_network(network, prev_location_b, cur_location_b)

    prev_location_a = cur_location_a
    prev_location_b = cur_location_b
    cur_location_a = next_location_a
    cur_location_b = next_location_b

    path_a.add(cur_location_a)
    path_b.add(cur_location_b)

    if cur_location_a == cur_location_b:
        break

print(len(path_a))
