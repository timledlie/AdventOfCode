from collections import defaultdict

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
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        neighbor = x + dx, y + dy
        if (neighbor in path_locations) and (neighbor not in locations_traversed):
            valid_neighbors.append(neighbor)

    return valid_neighbors


def longest_path(cur, end, locations_traversed):
    if cur == end:
        return 0
    next_max_distances = []
    for next_node, distance in edges[cur].items():
        if next_node not in locations_traversed:
            rest_max_distance = longest_path(next_node, end, locations_traversed + [next_node])
            if rest_max_distance is not None:
                next_max_distances.append(distance + rest_max_distance)
    if len(next_max_distances) > 0:
        return max(next_max_distances)
    else:
        return None


nodes = {start, end}
for location, path_type in path_locations.items():
    two_right = (location[0] + 2, location[1])
    if (path_type == ">") and (two_right in path_locations) and (path_locations[two_right] == ">"):
        nodes.add((location[0] + 1, location[1]))

    two_down = (location[0], location[1] + 2)
    if (path_type == "v") and (two_down in path_locations) and (path_locations[two_down] == "v"):
        nodes.add((location[0], location[1] + 1))

edges = defaultdict(dict)  # {nodeA: {nodeB: weight,...}, ...}
for node in nodes:
    for cur in get_valid_neighbors(node, []):
        locations_traversed = [node, cur]
        n_steps = 1
        while True:
            cur = get_valid_neighbors(cur, locations_traversed)[0]
            n_steps += 1
            locations_traversed.append(cur)
            if cur in nodes:
                edges[node][cur] = n_steps
                edges[cur][node] = n_steps
                break

print(longest_path(start, end, [start]))
