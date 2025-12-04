with (open("input.txt") as f):
    grid = [line.strip() for line in f.readlines()]

n_rows, n_cols = len(grid), len(grid[0])

n_accessible = 0
for row in range(n_rows):
    for col in range(n_cols):
        if grid[row][col] == "@":
            n_adjacent = 0
            for r in (row - 1, row, row + 1):
                for c in (col - 1, col, col + 1):
                    if r < 0 or r >= n_rows or c < 0 or c >= n_cols or (r == row and c == col):
                        continue
                    if grid[r][c] == "@":
                        n_adjacent += 1
            if n_adjacent < 4:
                n_accessible += 1

print(n_accessible)
