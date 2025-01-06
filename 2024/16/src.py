grid = []
with open("input.txt") as file:
    for line in file.readlines():
        grid.append([c for c in line.strip()])

n_rows = len(grid)
n_cols = len(grid[0])

big_int = 10000000000000000
tiles = [
    [
        {0: {"cost": big_int, "past_tiles": set()},
         1: {"cost": big_int, "past_tiles": set()},
         2: {"cost": big_int, "past_tiles": set()},
         3: {"cost": big_int, "past_tiles": set()}
        } for col in range(n_cols)
    ] for row in range(n_rows)
]

row_start, col_start = None, None
row_end, col_end = None, None
for row in range(n_rows):
    for col in range(n_cols):
        if grid[row][col] == "S":
            row_start = row
            col_start = col
        elif grid[row][col] == "E":
            row_end = row
            col_end = col

# 0 is east, 1 is south, 2 is west, 3 is north
# rows increase from north to south, cols increase from west to east
step_map = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

frontier = {(row_start, col_start, 0)}
tiles[row_start][col_start][0]["cost"] = 0
tiles[row_start][col_start][0]["past_tiles"] = {(row_start, col_start)}
while len(frontier) > 0:
    frontier_next = set()
    for row, col, orientation in frontier:
        if (row == row_end) and (col == col_end):
            continue
        cost_cur = tiles[row][col][orientation]["cost"]
        if cost_cur == big_int:
            continue
        for orientation_change, cost_increment in ((0, 1), (-1, 1001), (1, 1001)):
            orientation_next = (orientation + orientation_change) % 4
            row_step, col_step = step_map[orientation_next]
            row_next, col_next = row + row_step, col + col_step
            cost_next = cost_cur + cost_increment
            if grid[row_next][col_next] != "#":
                if cost_next < tiles[row_next][col_next][orientation_next]["cost"]:
                    tiles[row_next][col_next][orientation_next]["cost"] = cost_next
                    tiles[row_next][col_next][orientation_next]["past_tiles"] = tiles[row][col][orientation]["past_tiles"] | {(row_next, col_next)}
                    frontier_next.add((row_next, col_next, orientation_next))
                elif cost_next == tiles[row_next][col_next][orientation_next]["cost"]:
                    tiles[row_next][col_next][orientation_next]["past_tiles"] |= tiles[row][col][orientation]["past_tiles"] | {(row_next, col_next)}
                    frontier_next.add((row_next, col_next, orientation_next))
    frontier = frontier_next

shortest_path = big_int
most_tiles = 0
for orientation in (0, 1, 2, 3):
    n_past_tiles = len(tiles[row_end][col_end][orientation]["past_tiles"])
    cost = tiles[row_end][col_end][orientation]["cost"]
    if cost <= shortest_path:
        most_tiles = max(most_tiles, n_past_tiles)
print(n_past_tiles)
