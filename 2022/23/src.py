def print_ground(ground):
    for row in ground:
        print(''.join(row))


def count_empty_tiles_in_smallest_region(ground):
    rows_with_elves = []
    for row in range(len(ground)):
        if '#' in ground[row]:
            rows_with_elves.append(row)
    min_row = rows_with_elves[0]
    max_row = rows_with_elves[-1]

    min_col, max_col = len(ground[0]), 0
    for row in range(len(ground)):
        for col in range(len(ground[0])):
            if ground[row][col] == '#':
                min_col = min(min_col, col)
                max_col = max(max_col, col)

    n_empty = 0
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if ground[row][col] == '.':
                n_empty += 1
    return n_empty


with open("input_sample.txt") as file:
    ground_orig = [list(line.strip()) for line in file.readlines()]

direction = 0

expand_by = 2
ground = [['.'] * (len(ground_orig[0]) + 2 * expand_by) for i in range(expand_by)]
for row in ground_orig:
    ground.append(['.'] * expand_by + row + ['.'] * expand_by)
ground += [['.'] * (len(ground_orig[0]) + 2 * expand_by) for i in range(expand_by)]


