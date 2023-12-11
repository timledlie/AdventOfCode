import itertools, sortedcontainers


def find_chasm_rows_and_cols(image):
    empty_rows, empty_cols = sortedcontainers.SortedSet(), sortedcontainers.SortedSet()
    for row in range(len(image)):
        is_empty_row = True
        for col in range(len(image[0])):
            if image[row][col] == "#":
                is_empty_row = False
                break
        if is_empty_row:
            empty_rows.add(row)

    for col in range(len(image[0])):
        is_empty_col = True
        for row in range(len(image)):
            if image[row][col] == "#":
                is_empty_col = False
                break
        if is_empty_col:
            empty_cols.add(col)

    return empty_rows, empty_cols


def get_galaxy_locations(image):
    galaxy_locations = []
    for row in range(len(image)):
        for col in range(len(image[0])):
            if image[row][col] == "#":
                galaxy_locations.append((row, col))
    return galaxy_locations


def count_subset_within_range(int_set, range_start, range_end):
    return len(list(int_set.irange(min(range_start, range_end), max(range_start, range_end))))


def distance_between_galaxies(a, b, chasm_rows, chasm_cols, chasm_size):
    distance_without_chasms = abs(a[0] - b[0]) + abs(a[1] - b[1])
    n_row_chasms_crossed = count_subset_within_range(chasm_rows, a[0], b[0])
    n_col_chasms_crossed = count_subset_within_range(chasm_cols, a[1], b[1])
    return distance_without_chasms \
        - n_row_chasms_crossed - n_col_chasms_crossed\
        + chasm_size * (n_row_chasms_crossed + n_col_chasms_crossed)


chasm_size = 1000000
with open("input.txt") as file:
    image = [list(line.strip()) for line in file.readlines()]

chasm_rows, chasm_cols = find_chasm_rows_and_cols(image)
galaxy_locations = get_galaxy_locations(image)

distances_sum = 0
for a, b in itertools.combinations(galaxy_locations, 2):
    distances_sum += distance_between_galaxies(a, b, chasm_rows, chasm_cols, chasm_size)

print(distances_sum)
