from collections import namedtuple


def solve_part_1(instructions):
    res = 0
    grid = {}

    for state, x_range, y_range, z_range in instructions:
        min_x, max_x = x_range
        min_y, max_y = y_range
        min_z, max_z = z_range

        if min_x < -50 or max_x > 50 or min_y < -50 or max_y > 50 or min_z < -50 or max_z > 50:
            continue

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    if state == 'off':
                        grid[x, y, z] = 0
                    else:
                        grid[x, y, z] = 1

    for k in grid:
        if grid[k] == 1:
            res += 1

    return res


Cuboid = namedtuple('Cuboid', ['min_x', 'max_x', 'min_y', 'max_y', 'min_z', 'max_z', 'sign'])


def intersect(cuboid_1, cuboid_2):
    if not (cuboid_1.min_x <= cuboid_2.max_x and cuboid_1.max_x >= cuboid_2.min_x):
        return False

    if not (cuboid_1.min_y <= cuboid_2.max_y and cuboid_1.max_y >= cuboid_2.min_y):
        return False

    if not (cuboid_1.min_z <= cuboid_2.max_z and cuboid_1.max_z >= cuboid_2.min_z):
        return False

    return True


def get_intersection(cuboid_1, cuboid_2):
    min_x = max(cuboid_1.min_x, cuboid_2.min_x)
    max_x = min(cuboid_1.max_x, cuboid_2.max_x)

    min_y = max(cuboid_1.min_y, cuboid_2.min_y)
    max_y = min(cuboid_1.max_y, cuboid_2.max_y)

    min_z = max(cuboid_1.min_z, cuboid_2.min_z)
    max_z = min(cuboid_1.max_z, cuboid_2.max_z)

    sign = -1 * cuboid_2.sign

    return Cuboid(min_x, max_x, min_y, max_y, min_z, max_z, sign)


def get_volume(cuboid):
    return (cuboid.max_x - cuboid.min_x + 1) * (cuboid.max_y - cuboid.min_y + 1) * (cuboid.max_z - cuboid.min_z + 1)


def solve_part_2(instructions):
    cuboids = []

    for state, x_range, y_range, z_range in instructions:
        min_x, max_x = x_range
        min_y, max_y = y_range
        min_z, max_z = z_range

        curr = Cuboid(min_x, max_x, min_y, max_y, min_z, max_z, -1 if state == 'off' else 1)
        intersections = []

        for cuboid in cuboids:
            if intersect(curr, cuboid):
                intersection = get_intersection(curr, cuboid)
                intersections.append(intersection)

        for intersection in intersections:
            cuboids.append(intersection)

        if state == 'on':
            cuboids.append(curr)

    res = 0

    for cuboid in cuboids:
        res += get_volume(cuboid) * cuboid.sign

    return res


with open('input.txt') as f:
    instructions = []

    for line in f.readlines():
        line = line.strip()

        state, ranges = line.split(' ')
        x_range, y_range, z_range = ranges.split(',')

        x_range = x_range.split('=')[1]
        min_x, max_x = x_range.split('..')
        min_x, max_x = int(min_x), int(max_x)

        y_range = y_range.split('=')[1]
        min_y, max_y = y_range.split('..')
        min_y, max_y = int(min_y), int(max_y)

        z_range = z_range.split('=')[1]
        min_z, max_z = z_range.split('..')
        min_z, max_z = int(min_z), int(max_z)

        instructions.append([state, (min_x, max_x), (min_y, max_y), (min_z, max_z)])

    print(solve_part_2(instructions))