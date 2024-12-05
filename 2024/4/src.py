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

xmas_count = 0
for row in range(n_buffer, n_rows + n_buffer):
    for col in range(n_buffer, n_cols + n_buffer):
        if grid[row][col] == 'A':
            if grid[row - 1][col - 1] == "M" and grid[row + 1][col - 1] == "M" and \
               grid[row - 1][col + 1] == "S" and grid[row + 1][col + 1] == "S":
                xmas_count += 1
            if grid[row - 1][col + 1] == "M" and grid[row + 1][col + 1] == "M" and \
               grid[row - 1][col - 1] == "S" and grid[row + 1][col - 1] == "S":
                xmas_count += 1
            if grid[row + 1][col - 1] == "M" and grid[row + 1][col + 1] == "M" and \
               grid[row - 1][col - 1] == "S" and grid[row - 1][col + 1] == "S":
                xmas_count += 1
            if grid[row - 1][col - 1] == "M" and grid[row - 1][col + 1] == "M" and \
               grid[row + 1][col - 1] == "S" and grid[row + 1][col + 1] == "S":
                xmas_count += 1

print(xmas_count)
