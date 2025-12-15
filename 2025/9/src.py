import itertools

with (open("input.txt") as f):
    red_tile_coords = [tuple(map(int, line.split(','))) for line in f.readlines()]

max_area = 0
for (x1, y1), (x2, y2) in itertools.combinations(red_tile_coords, 2):
    max_area = max(max_area, (abs(x1 - x2) + 1 ) * (abs(y1 - y2) + 1))

print(max_area)
