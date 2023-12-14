def tilt_north(platform):
    for row_index in range(1, len(platform)):
        for col_index in range(len(platform[0])):
            if platform[row_index][col_index] == "O":
                platform[row_index][col_index] = "."
                for r in range(row_index, -1, -1):
                    if (r == 0) or (platform[r - 1][col_index] != "."):
                        platform[r][col_index] = "O"
                        break


def tilt_west(platform):
    for col_index in range(1, len(platform[0])):
        for row_index in range(len(platform)):
            if platform[row_index][col_index] == "O":
                platform[row_index][col_index] = "."
                for c in range(col_index, -1, -1):
                    if (c == 0) or (platform[row_index][c - 1] != "."):
                        platform[row_index][c] = "O"
                        break


def tilt_south(platform):
    for row_index in range(len(platform) - 2, -1, -1):
        for col_index in range(len(platform[0])):
            if platform[row_index][col_index] == "O":
                platform[row_index][col_index] = "."
                for r in range(row_index, len(platform)):
                    if (r == (len(platform) - 1)) or (platform[r + 1][col_index] != "."):
                        platform[r][col_index] = "O"
                        break


def tilt_east(platform):
    for col_index in range(len(platform[0]) - 2, -1, -1):
        for row_index in range(len(platform)):
            if platform[row_index][col_index] == "O":
                platform[row_index][col_index] = "."
                for c in range(col_index, len(platform[0])):
                    if (c == (len(platform[0]) - 1)) or (platform[row_index][c + 1] != "."):
                        platform[row_index][c] = "O"
                        break


def calculate_north_load(platform):
    total_load = 0
    for row_index, weight in zip(range(len(platform)), range(len(platform), 0, -1)):
        total_load += weight * platform[row_index].count("O")
    return total_load


with open("input.txt") as file:
    platform = [list(line.strip()) for line in file.readlines()]

while True:
    tilt_north(platform)
    tilt_west(platform)
    tilt_south(platform)
    tilt_east(platform)
    print(calculate_north_load(platform))

# Abort program after a few seconds, look for longest repeating pattern ("longest") and 1-based index of the first
# time it starts repeating ("start_repeat"), then
# (1B - start_repeat) % longest
# is the 0-based index into the repeating pattern that gives the answer
