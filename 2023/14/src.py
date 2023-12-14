def tilt_north(platform):
    for row_index in range(1, len(platform)):
        for col_index in range(len(platform[0])):
            if platform[row_index][col_index] == "O":
                platform[row_index][col_index] = "."
                for r in range(row_index, -1, -1):
                    if (r == 0) or (platform[r - 1][col_index] != "."):
                        platform[r][col_index] = "O"
                        break


def calculate_north_load(platform):
    total_load = 0
    for row_index, weight in zip(range(len(platform)), range(len(platform), 0, -1)):
        total_load += weight * platform[row_index].count("O")
    return total_load


with open("input.txt") as file:
    platform = [list(line.strip()) for line in file.readlines()]

tilt_north(platform)
print(calculate_north_load(platform))
