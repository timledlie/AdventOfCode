with open("input.txt") as file:
    grid = [[int(c) for c in line.strip()] for line in file.readlines()]

dim = len(grid)
count_perimeter = 2 * 2 * dim - 4


def is_visible(grid, dim, row, col):
    height = grid[row][col]
    hidden_count = 0
    for r in range(0, row):
        if grid[r][col] >= height:
            hidden_count += 1
            break
    for r in range(row + 1, dim):
        if grid[r][col] >= height:
            hidden_count += 1
            break
    for c in range(0, col):
        if grid[row][c] >= height:
            hidden_count += 1
            break
    for c in range(col + 1, dim):
        if grid[row][c] >= height:
            hidden_count += 1
            break
    return hidden_count < 4


def scenic_score(grid, dim, row, col):
    height = grid[row][col]
    score = 1

    count_visible = 0
    for r in range(row - 1, -1, -1):
        count_visible += 1
        if grid[r][col] >= height:
            break
    score *= count_visible

    count_visible = 0
    for c in range(col - 1, -1, -1):
        count_visible += 1
        if grid[row][c] >= height:
            break
    score *= count_visible

    count_visible = 0
    for c in range(col + 1, dim):
        count_visible += 1
        if grid[row][c] >= height:
            break
    score *= count_visible

    count_visible = 0
    for r in range(row + 1, dim):
        count_visible += 1
        if grid[r][col] >= height:
            break
    score *= count_visible

    return score


max_score = 0
for row in range(1, dim - 1):
    for col in range(1, dim - 1):
        score = scenic_score(grid, dim, row, col)
        max_score = max(max_score, score)

print(max_score)