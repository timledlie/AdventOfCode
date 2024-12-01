from collections import defaultdict
import copy
import itertools

maze_locations = []
object_locations = {}
key_names, door_names = [], []
x, y = 0, 0
with open("input_sample.txt") as file:
    for line in file.readlines():
        line = line.strip()
        for char in line:
            if char != "#":
                maze_locations.append((x, y))
                if char != ".":
                    object_locations[(x, y)] = char
                    object_locations[char] = (x, y)
                    if char.islower():
                        key_names.append(char)
                    elif char.isupper():
                        door_names.append(char)
            x += 1
        x = 0
        y += 1

n_objects = len(key_names) + len(door_names)


def bfs_adjacent_objects(starting_object):
    maze_locations_set = set(maze_locations)
    visited_locations = {object_locations[starting_object]}
    frontier = [object_locations[starting_object]]
    first_objects = []
    first_objects_distances = {}
    distance = 1
    while frontier:
        frontier_next = []
        for x, y in frontier:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                adjacent = x + dx, y + dy
                if adjacent not in visited_locations and adjacent in maze_locations_set:
                    visited_locations.add(adjacent)
                    if adjacent in object_locations:
                        object_name = object_locations[adjacent]
                        first_objects.append(object_name)
                        first_objects_distances[object_name] = distance
                    else:
                        frontier_next.append(adjacent)
        distance += 1
        frontier = frontier_next

    return first_objects, first_objects_distances


first_objects, first_objects_distances = bfs_adjacent_objects("@")
print(first_objects)
print(first_objects_distances)
del object_locations[object_locations["@"]]
del object_locations["@"]

graph = defaultdict(list)
distances = defaultdict(int)
for obj in object_locations:
    if type(obj) == tuple:
        continue
    adjacent_objects, adjacent_objects_distances = bfs_adjacent_objects(obj)
    for adjacent_object in adjacent_objects:
        graph[obj].append(adjacent_object)
    for adjacent_object, distance in adjacent_objects_distances.items():
        distances[(obj, adjacent_object)] = distance

print(graph)
print(distances)


def is_valid_next_object(next_object, objects_visited):
    if next_object.islower():
        return True
    return next_object.lower() in objects_visited


big_number = 100000000000000


def remove_object(cur_object, graph, distances):
    new_graph = copy.deepcopy(graph)
    for a, b in itertools.combinations(graph[cur_object], 2):
        d = distances[(a, cur_object)] + distances[(b, cur_object)]
        distances[(a, b)] = d
        distances[(b, a)] = d
        if cur_object in new_graph[a]:
            new_graph[a].remove(cur_object)
        if cur_object in new_graph[b]:
            new_graph[b].remove(cur_object)
        if b not in new_graph[a]:
            new_graph[a].append(b)
        if a not in new_graph[b]:
            new_graph[b].append(a)
    return new_graph, distances


memo = {}
def shortest_path(cur_object, cur_distance, objects_visited, graph, distances):
    memo_key = (cur_object, cur_distance, tuple(objects_visited))
    if memo_key in memo:
        return memo[memo_key]

    if len(objects_visited) == n_objects:
        return cur_distance

    next_shortest_paths = [big_number]
    for next_object in graph[cur_object]:
        if is_valid_next_object(next_object, objects_visited):
            next_graph, next_distances = remove_object(cur_object, graph, distances)
            next_shortest_paths.append(shortest_path(next_object, distances[(cur_object, next_object)], objects_visited + [next_object], next_graph, next_distances))

    result = cur_distance + min(next_shortest_paths)
    memo[memo_key] = result
    return result


min_distance = big_number
for first_object in first_objects:
    if first_object.isupper():
        continue
    min_distance = min(min_distance, shortest_path(first_object, first_objects_distances[first_object], [first_object], graph, distances))
print(min_distance)
