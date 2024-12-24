with open("input.txt") as file:
    input_text = file.read()

grid_text, movements_text = input_text.split("\n\n")

grid = []
row = 0
for line in grid_text.strip().split("\n"):
    row = []
    for c in line:
        if c in ("#", "."):
            row.extend([c, c])
        if c == "O":
            row.extend(["[", "]"])
        if c == "@":
            row.extend(["@", "."])
    grid.append(row)

n_rows, n_cols = len(grid), len(grid[0])
robot_row, robot_col = None, None
for row in range(n_rows):
    for col in range(n_cols):
        if grid[row][col] == "@":
            robot_row, robot_col = row, col


def try_to_move_up_down(grid, r, c, d_r):
    if grid[r][c] == ".":
        return [], True
    if grid[r][c] == "#":
        return [], False
    if grid[r][c] == "]":
        c -= 1
    blocks_to_move = {(r, c)}
    cur_row_blocks = {(r, c)}
    while len(cur_row_blocks) > 0:
        next_row_blocks = set()
        r += d_r
        for block in cur_row_blocks:
            adjacent_left = grid[r][block[1]]
            adjacent_right = grid[r][block[1] + 1]
            if (adjacent_left == "#") or (adjacent_right == "#"):
                return None, False
            if (adjacent_left == "[") or (adjacent_right == "]"):
                next_row_blocks.add((r, block[1]))
            if adjacent_left == "]":
                next_row_blocks.add((r, block[1] - 1))
            if adjacent_right == "[":
                next_row_blocks.add((r, block[1] + 1))
        cur_row_blocks = next_row_blocks
        blocks_to_move.update(next_row_blocks)
    return blocks_to_move, True


movements = [c for c in movements_text.replace("\n", "")]

movement_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
for m in movements:
    d_r, d_c = movement_map[m]
    r, c = robot_row + d_r, robot_col + d_c
    if m in ("<", ">"):
        while grid[r][c] in ("[", "]"):
            c += d_c
        if grid[r][c] == ".":
            for col in range(c, robot_col + d_c, -1 * d_c):
                grid[r][col] = grid[r][col - d_c]
            grid[robot_row][robot_col] = "."
            robot_col += d_c
            grid[robot_row][robot_col] = "@"
    else:
        blocks_to_move, can_move = try_to_move_up_down(grid, r, c, d_r)
        if can_move:
            new_blocks = []
            for block_to_move in blocks_to_move:
                new_blocks.append((block_to_move[0] + d_r, block_to_move[1]))
                grid[block_to_move[0]][block_to_move[1]] = "."
                grid[block_to_move[0]][block_to_move[1] + 1] = "."
            for new_block in new_blocks:
                grid[new_block[0]][new_block[1]] = "["
                grid[new_block[0]][new_block[1] + 1] = "]"
            grid[robot_row][robot_col] = "."
            robot_row += d_r
            grid[robot_row][robot_col] = "@"

gps = 0
for row in range(n_rows):
    for col in range(n_cols):
        if grid[row][col] == "[":
            gps += (100 * row) + col
print(gps)
