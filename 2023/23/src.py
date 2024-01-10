path_locations = {}
with open("input.txt") as file:
    lines = file.readlines()
    x_max, y_max = len(lines[0]) - 2, len(lines) - 1
    start, end = (1, 0), (x_max - 1, y_max)
    for y in range(len(lines)):
        line = lines[y].strip()
        for x in range(len(line)):
            if line[x] != "#":
                path_locations[(x, y)] = line[x]


def get_valid_neighbors(location, locations_traversed):
    x, y = location
    valid_neighbors = []
    for dx, dy, uphill in ((1, 0, "<"), (-1, 0, ">"), (0, 1, "^"), (0, -1, "v")):
        neighbor = x + dx, y + dy
        if (neighbor in path_locations) and (path_locations[neighbor] != uphill) and (neighbor not in locations_traversed):
            valid_neighbors.append(neighbor)

    return valid_neighbors


def longest_path(start, end, locations_traversed):
    n_steps = 0
    cur = start
    while True:
        valid_neighbors = get_valid_neighbors(cur, locations_traversed)
        if len(valid_neighbors) == 0:
            return 0
        elif len(valid_neighbors) == 1:
            n_steps += 1
            cur = valid_neighbors[0]
            locations_traversed.append(cur)
            if cur == end:
                return n_steps
        else:
            return n_steps + 1 + max([longest_path(neighbor, end, locations_traversed + [neighbor]) for neighbor in valid_neighbors])


print(longest_path(start, end, [start]))
