grid = []
with open("input.txt") as file:
    for line in file.readlines():
        grid.append([c for c in line.strip()])

n_rows = len(grid)
n_cols = len(grid[0])

big_int = 10000000000000000000
grid_shortest_path = [[big_int for col in range(n_cols)] for row in range(n_rows)]

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
grid[row_start][col_start] = "."
grid[row_end][col_end] = "."

# 0 is east, 1 is south, 2 is west, 3 is north
# rows increase from north to south, cols increase from west to east
step_map = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

frontier = [(row_start, col_start, 0, 0)]
grid_shortest_path[row_start][row_end] = 0
while len(frontier) > 0:
    frontier_next = []
    for row, col, orientation, cost in frontier:
        for orientation_change, cost_change in ((0, 1), (-1, 1001), (1, 1001)):
            orientation_next = (orientation + orientation_change) % 4
            row_step, col_step = step_map[orientation_next]
            row_next, col_next = row + row_step, col + col_step
            cost_next = cost + cost_change
            if (grid[row_next][col_next] == ".") and (cost_next < grid_shortest_path[row_next][col_next]):
                grid_shortest_path[row_next][col_next] = cost_next
                frontier_next.append((row_next, col_next, orientation_next, cost_next))
    frontier = frontier_next

print(grid_shortest_path[row_end][col_end])
