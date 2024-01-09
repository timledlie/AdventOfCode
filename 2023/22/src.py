from collections import defaultdict
import copy


def get_brick_footprint(brick):
    footprint = set()
    (x1, y1, z1), (x2, y2, z2) = brick
    if x1 != x2:
        for x in range(x1, x2 + 1):
            footprint.add((x, y1))
    else:
        for y in range(y1, y2 + 1):
            footprint.add((x1, y))
    return footprint


def drop_brick(highest_blocks, brick):
    z_landing = 0
    footprint = get_brick_footprint(brick)
    for x, y in footprint:
        z_landing = max(z_landing, highest_blocks[(x, y)])
    z_landing += 1
    for x, y in footprint:
        highest_blocks[(x, y)] = z_landing

    (x1, y1, z1), (x2, y2, z2) = brick
    if z2 > z1:
        highest_blocks[(x, y)] += (z2 - z1)

    return (x1, y1, z_landing), (x2, y2, z2 - z1 + z_landing)


def drop_bricks(bricks):
    # sort by z
    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))
    highest_blocks = defaultdict(int)
    settled_bricks = []
    for brick in bricks:
        settled_bricks.append(drop_brick(highest_blocks, brick))
    return settled_bricks


bricks = []
x_max, y_max = 0, 0
with open("input.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split("~")
        x1, y1, z1 = tuple(map(int, a.split(",")))
        x2, y2, z2 = tuple(map(int, b.split(",")))
        x_max = max(x_max, x1, x2)
        y_max = max(y_max, y1, y2)
        bricks.append(((x1, y1, z1), (x2, y2, z2)))

n_disintegratable_bricks = 0
settled_bricks = drop_bricks(bricks)
for brick in settled_bricks:
    bricks = copy.copy(settled_bricks)
    bricks.remove(brick)
    if bricks == drop_bricks(bricks):
        n_disintegratable_bricks += 1

print(n_disintegratable_bricks)
