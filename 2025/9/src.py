import itertools
from shapely.geometry import Point, Polygon

with (open("input.txt") as f):
    red_tile_coords = [tuple(map(int, line.split(','))) for line in f.readlines()]

polygon = Polygon(red_tile_coords)

max_area = 0
for (x1, y1), (x2, y2) in itertools.combinations(red_tile_coords, 2):
    rectangle = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
    if polygon.covers(rectangle):
        max_area = max(max_area, (abs(x1 - x2) + 1 ) * (abs(y1 - y2) + 1))

print(max_area)
