import itertools

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


def filter_shortest(paths):
    min_length = min(len(path) for path in paths)
    return list(filter(lambda path: len(path) == min_length, paths))


def get_keypad_min_paths(keypad, code):
    paths = [path + 'A' for path in keypad[('A', code[0])]]
    for i in range(len(code) - 1):
        paths_next = []
        paths_step = keypad[(code[i], code[i+1])]
        for path in paths:
            for path_step in paths_step:
                paths_next.append(path + path_step + 'A')
        paths = paths_next
    return filter_shortest(paths)


numeric_keypad_paths = get_all_paths(numeric_keypad)
directional_keypad_paths = get_all_paths(directional_keypad)

sum_complexities = 0
for code in codes:
    paths1 = get_keypad_min_paths(numeric_keypad_paths, code)

    paths2 = []
    for path in paths1:
        paths2.extend(get_keypad_min_paths(directional_keypad_paths, path))
    paths2 = filter_shortest(paths2)

    paths3 = []
    for path in paths2:
        paths3.extend(get_keypad_min_paths(directional_keypad_paths, path))
    paths3 = filter_shortest(paths3)

    sum_complexities += (int(code[:-1]) * len(paths3[0]))

print(sum_complexities)
