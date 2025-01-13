import itertools


def is_track(c):
    return c in (".", "S", "E")


with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

n_rows, n_cols = len(grid), len(grid[0])
track = set()
start, end = None, None
for row in range(n_rows):
    for col in range(n_cols):
        char = grid[row][col]
        coords = (row, col)
        if char == "S":
            start = coords
            track.add(coords)
        elif char == "E":
            end = coords
            track.add(coords)
        elif char == ".":
            track.add(coords)

row, col = start
pico_from_start = {start: 0}
visited = {start}
pico = 0
while (row, col) != end:
    pico += 1
    for (d_row, d_col) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        row_next, col_next = row + d_row, col + d_col
        if (row_next, col_next) not in visited and (row_next, col_next) in track:
            pico_from_start[(row_next, col_next)] = pico
            visited.add((row_next, col_next))
            break
    row, col = row_next, col_next

pico_saved_threshold = 100
cheat_max = 20
count = 0
for cheat_start, cheat_end in itertools.combinations(track, 2):
    distance = abs(cheat_start[0] - cheat_end[0]) + abs(cheat_start[1] - cheat_end[1])
    if (distance <= cheat_max) and \
       (abs(pico_from_start[cheat_start] - pico_from_start[cheat_end]) - distance) >= pico_saved_threshold:
        count += 1

print(count)
