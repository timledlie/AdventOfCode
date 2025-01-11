def is_track(c):
    return c in (".", "S", "E")


with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

n_rows, n_cols = len(grid), len(grid[0])
walls, track = set(), set()
cheats_vertical, cheats_horizontal = [], []
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
        else:
            walls.add(coords)
            if (0 < row < n_rows - 1) and (0 < col < n_cols - 1):
                if is_track(grid[row - 1][col]) and is_track(grid[row + 1][col]):
                    cheats_vertical.append(coords)
                if is_track(grid[row][col - 1]) and is_track(grid[row][col + 1]):
                    cheats_horizontal.append(coords)

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

pico_start_to_end = pico_from_start[end]
threshold = 100
count = 0
for (row, col) in cheats_vertical:
    if (abs(pico_from_start[(row - 1, col)] - pico_from_start[(row + 1, col)]) - 2) >= threshold:
        count += 1
for (row, col) in cheats_horizontal:
    if (abs(pico_from_start[(row, col - 1)] - pico_from_start[(row, col + 1)]) - 2) >= threshold:
        count += 1

print(count)
