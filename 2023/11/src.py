import itertools


def find_empty_rows_and_cols(image):
    empty_rows, empty_cols = set(), set()
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


def expand_universe(image):
    empty_rows, empty_cols = find_empty_rows_and_cols(image)
    image_expanded = []
    for row in range(len(image)):
        row_expanded = []
        for col in range(len(image[0])):
            row_expanded.append(image[row][col])
            if col in empty_cols:
                row_expanded.append(".")
        image_expanded.append(row_expanded)
        if row in empty_rows:
            image_expanded.append(["."] * (len(image[0]) + len(empty_cols)))
    return image_expanded


def get_galaxy_locations(image):
    galaxy_locations = []
    for row in range(len(image)):
        for col in range(len(image[0])):
            if image[row][col] == "#":
                galaxy_locations.append((row, col))
    return galaxy_locations


def distance_between_galaxies(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open("input_sample.txt") as file:
    image = [list(line.strip()) for line in file.readlines()]

image = expand_universe(image)
galaxy_locations = get_galaxy_locations(image)

distances_sum = 0
for a, b in itertools.combinations(galaxy_locations, 2):
    distances_sum += distance_between_galaxies(a, b)

print(distances_sum)
