import itertools
import copy

with open("input.txt") as file:
    codes = [line.strip() for line in file.readlines()]

numeric_keypad = {
    'A': (('<', '0'), ('^', '3')),
    '0': (('>', 'A'), ('^', '2')),
    '1': (('>', '2'), ('^', '4')),
    '2': (('v', '0'), ('<', '1'), ('>', '3'), ('^', '5')),
    '3': (('v', 'A'), ('<', '2'), ('^', '6')),
    '4': (('v', '1'), ('>', '5'), ('^', '7')),
    '5': (('v', '2'), ('<', '4'), ('>', '6'), ('^', '8')),
    '6': (('v', '3'), ('<', '5'), ('^', '9')),
    '7': (('v', '4'), ('>', '8')),
    '8': (('v', '5'), ('<', '7'),  ('>', '9')),
    '9': (('v', '6'), ('<', '8'))
}

directional_keypad = {
    'A': (('v', '>'), ('<', '^')),
    '^': (('>', 'A'), ('v', 'v')),
    '>': (('^', 'A'), ('<', 'v')),
    'v': (('^', '^'), ('>', '>'), ('<', '<')),
    '<': (('>', 'v'),)
}


def get_paths_for_pair(a, b, keypad):
    paths = []
    frontier = [(a, '')]
    finished = False
    while not finished:
        frontier_next = []
        for (k, path) in frontier:
            if k == b:
                finished = True
                paths.append(path)
            else:
                for (step, next_key) in keypad[k]:
                    frontier_next.append((next_key, path + step))
        frontier = frontier_next
    return paths


def get_all_paths(keypad):
    keypad_options = keypad.keys()
    keypad_paths = {}
    for (a, b) in itertools.permutations(keypad_options, 2):
        keypad_paths[(a, b)] = get_paths_for_pair(a, b, keypad)
    for a in keypad_options:
        keypad_paths[(a, a)] = ['']
    return keypad_paths


def get_keypad_min_paths(keypad, code):
    paths = [path + 'A' for path in keypad[('A', code[0])]]
    for i in range(len(code) - 1):
        paths_next = []
        paths_step = keypad[(code[i], code[i+1])]
        for path in paths:
            for path_step in paths_step:
                paths_next.append(path + path_step + 'A')
        paths = paths_next
    return paths


counts_map = {
    "": 0,
    "^": 0,
    ">": 0,
    "v": 0,
    "<": 0,
    '>^': 0,
    '>v': 0,
    'v>': 0,
    'v<': 0,
    '^>': 0,
    '<v': 0,
    '<^': 0,
    '^<': 0,
    ">>^": 0,
    "v<<": 0,
    ">^>": 0,
    "<v<": 0
}


def convert_path_to_map(path):
    counts = copy.copy(counts_map)
    for pattern in path.split('A')[:-1]:
        counts[pattern] += 1
    return counts


# For tie-breaks (eg. <v vs v<), I ran simulations and selected for the shortest resulting patterns
def get_next_pattern(pattern):
    if pattern == '':
        return '',
    if pattern == '^':
        return '<', '>'
    if pattern == '>':
        return 'v', '^'
    if pattern == 'v':
        return '<v', '^>'
    if pattern == '<':
        return 'v<<', '>>^'
    if pattern == '^>':
        return '<', 'v>', '^'
    if pattern == '^<':
        return '<', 'v<', '>>^'
    if pattern == '>^':
        return 'v', '<^', '>'
    if pattern == '>v':
        return 'v', '<', '^>'
    if pattern == 'v>':
        return '<v', '>', '^'
    if pattern == 'v<':
        return '<v', '<', '>>^'
    if pattern == '<^':
        return 'v<<', '>^', '>'  # only case where >^ used instead of ^> (since ^> is invalid here)
    if pattern == '<v':
        return 'v<<', '>', '^>'
    if pattern == '>>^':
        return 'v', '', '<^', '>'
    if pattern == 'v<<':
        return '<v', '<', '', '>>^'
    if pattern == '>^>':
        return 'v', '<^', 'v>', '^'
    if pattern == '<v<':
        return 'v<<', '>', '<', '>>^'


def get_path_map_length(path_map):
    length = 0
    for pattern, n in path_map.items():
        length += n * (len(pattern) + 1)
    return length


numeric_keypad_paths = get_all_paths(numeric_keypad)
directional_keypad_paths = get_all_paths(directional_keypad)

n_rounds = 25
sum_complexities = 0
for code in codes:
    paths = get_keypad_min_paths(numeric_keypad_paths, code)

    paths_next = []
    for path in paths:
        more_paths = get_keypad_min_paths(directional_keypad_paths, path)
        paths_next.extend(more_paths)
    paths = paths_next

    path_maps = [convert_path_to_map(path) for path in paths]

    for r in range(n_rounds - 1):
        path_maps_next = []
        for path_map in path_maps:
            path_map_next = copy.copy(counts_map)
            for pattern, n in path_map.items():
                for p in get_next_pattern(pattern):
                    path_map_next[p] += n
            path_maps_next.append(path_map_next)
        path_maps = path_maps_next

    min_length = min(get_path_map_length(pm) for pm in path_maps)
    sum_complexities += int(code[:-1]) * min_length

print(sum_complexities)
