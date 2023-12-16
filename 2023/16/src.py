import sys
sys.setrecursionlimit(4000)


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


objects = {}
with open("input.txt") as file:
    grid_lines = [line.strip() for line in file.readlines()]
    n_rows, n_cols = len(grid_lines), len(grid_lines[0])
    for row_index in range(n_rows):
        for col_index in range(n_cols):
            char = grid_lines[row_index][col_index]
            if char in ("/", "\\", "|", "-"):
                objects[(row_index, col_index)] = char

energized_tile_log = set()
follow_light_path(0, 0, "right")

energized_tiles = set()
for tile in energized_tile_log:
    energized_tiles.add((tile[0], tile[1]))

print(len(energized_tiles))
