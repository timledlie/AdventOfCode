import itertools

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

n_rows = len(lines)
n_cols = len(lines[0])
n_buffer = 3
row_buffer = ['|' * (n_cols + 2 * n_buffer) for n in range(n_buffer)]
col_buffer = '|' * n_buffer

grid = []
grid += row_buffer
grid += [col_buffer + line + col_buffer for line in lines]
grid += row_buffer

deltas = list(itertools.product((-1, 0, 1), repeat=2))
deltas.remove((0, 0))

xmas_count = 0
for row in range(n_buffer, n_rows + n_buffer):
    for col in range(n_buffer, n_cols + n_buffer):
        if grid[row][col] == 'X':
            for delta_row, delta_col in deltas:
                if grid[row + 1 * delta_row][col + 1 * delta_col] == 'M' and \
                   grid[row + 2 * delta_row][col + 2 * delta_col] == 'A' and \
                   grid[row + 3 * delta_row][col + 3 * delta_col] == 'S':
                    xmas_count += 1

print(xmas_count)
