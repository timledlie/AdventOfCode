import sys
sys.setrecursionlimit(5000)

energized_tile_log = set()


def follow_light_path(row, col, direction):
    if (row < 0) or (row >= n_rows) or (col < 0) or (col >= n_cols):
        return

    if (row, col, direction) in energized_tile_log:
        return

    energized_tile_log.add((row, col, direction))
    if (row, col) in objects:
        object = objects[(row, col)]
        if object == "/":
            if direction == "right":
                return follow_light_path(row - 1, col, "up")
            if direction == "down":
                return follow_light_path(row, col - 1, "left")
            if direction == "left":
                return follow_light_path(row + 1, col, "down")
            if direction == "up":
                return follow_light_path(row, col + 1, "right")
        if object == "\\":
            if direction == "right":
                return follow_light_path(row + 1, col, "down")
            if direction == "down":
                return follow_light_path(row, col + 1, "right")
            if direction == "left":
                return follow_light_path(row - 1, col, "up")
            if direction == "up":
                return follow_light_path(row, col - 1, "left")
        if object == "|":
            if direction in ("right", "left"):
                follow_light_path(row - 1, col, "up")
                follow_light_path(row + 1, col, "down")
                return
            if direction == "down":
                return follow_light_path(row + 1, col, "down")
            if direction == "up":
                return follow_light_path(row - 1, col, "up")
        if object == "-":
            if direction in ("down", "up"):
                follow_light_path(row, col - 1, "left")
                follow_light_path(row, col + 1, "right")
                return
            if direction == "right":
                return follow_light_path(row, col + 1, "right")
            if direction == "left":
                return follow_light_path(row, col - 1, "left")

    if direction == "right":
        return follow_light_path(row, col + 1, "right")
    if direction == "down":
        return follow_light_path(row + 1, col, "down")
    if direction == "left":
        return follow_light_path(row, col - 1, "left")
    if direction == "up":
        return follow_light_path(row - 1, col, "up")


def n_energized_tiles(start_row, start_col, start_direction):
    global energized_tile_log
    energized_tile_log = set()
    follow_light_path(start_row, start_col, start_direction)

    energized_tiles = set()
    for tile in energized_tile_log:
        energized_tiles.add((tile[0], tile[1]))
    return len(energized_tiles)


objects = {}
with open("input.txt") as file:
    grid_lines = [line.strip() for line in file.readlines()]
    n_rows, n_cols = len(grid_lines), len(grid_lines[0])
    for row_index in range(n_rows):
        for col_index in range(n_cols):
            char = grid_lines[row_index][col_index]
            if char in ("/", "\\", "|", "-"):
                objects[(row_index, col_index)] = char

n_max = 0
for row_index in range(n_rows):
    n_max = max(n_max, n_energized_tiles(row_index, 0, "right"))
    n_max = max(n_max, n_energized_tiles(row_index, n_cols - 1, "left"))
for col_index in range(n_cols):
    n_max = max(n_max, n_energized_tiles(0, col_index, "down"))
    n_max = max(n_max, n_energized_tiles(n_rows - 1, col_index, "up"))

print(n_max)
