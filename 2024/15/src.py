with open("input.txt") as file:
    input_text = file.read()

grid_text, movements_text = input_text.split("\n\n")

grid = []
row = 0
for line in grid_text.strip().split("\n"):
    grid.append([c for c in line])

n_rows, n_cols = len(grid), len(grid[0])
robot_row, robot_col = None, None
for row in range(n_rows):
    for col in range(n_cols):
        if grid[row][col] == "@":
            robot_row, robot_col = row, col

movements = [c for c in movements_text.replace("\n", "")]

movement_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
for m in movements:
    d_r, d_c = movement_map[m]
    r, c = robot_row + d_r, robot_col + d_c
    while grid[r][c] == "O":
        r += d_r
        c += d_c
    if grid[r][c] == ".":
        grid[r][c] = "O"
        grid[robot_row][robot_col] = "."
        robot_row += d_r
        robot_col += d_c
        grid[robot_row][robot_col] = "@"

gps = 0
for row in range(n_rows):
    for col in range(n_cols):
        if grid[row][col] == "O":
            gps += (100 * row) + col
print(gps)
