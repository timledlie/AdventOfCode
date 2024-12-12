grid = []
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        grid.append(["."] + [char for char in line] + ["."])

grid = [["."] * len(grid[0])] + grid + [["."] * len(grid[0])]
n_rows, n_cols = len(grid), len(grid[0])


def find_new_region_start(points_processed, grid):
    n_rows, n_cols = len(grid), len(grid[0])
    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            if (row, col) not in points_processed:
                points_processed.add((row, col))
                return row, col
    return None


def walk_next_region(points_processed, grid):
    row, col = find_new_region_start(points_processed, grid)
    crop_type = grid[row][col]
    new_region = {(row, col)}
    frontier = {(row, col)}
    while True:
        frontier_next = set()
        for row, col in frontier:
            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                candidate = row + delta_row, col + delta_col
                if (crop_type == grid[row + delta_row][col + delta_col]) and \
                   (candidate not in points_processed) and \
                   (candidate not in frontier) and \
                   (candidate not in frontier_next) and \
                   (candidate not in new_region):
                    points_processed.add(candidate)
                    frontier_next.add(candidate)
                    new_region.add(candidate)
        if len(frontier_next) == 0:
            break
        frontier = frontier_next

    return new_region


points_processed = set()
regions = []
while len(points_processed) < ((n_rows - 2) * (n_cols - 2)):
    new_region = walk_next_region(points_processed, grid)
    regions.append(new_region)


def get_region_perimeter(region):
    perimeter = 0
    for row, col in region:
        for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            candidate = row + delta_row, col + delta_col
            if candidate not in region:
                perimeter += 1
    return perimeter


total_fencing_price = 0
for region in regions:
    total_fencing_price += len(region) * get_region_perimeter(region)
print(total_fencing_price)
