def surface_area(cubes):
    n = 0
    for cube in cubes:
        n += 6
        for x in (-1, 1):
            if (cube[0] + x, cube[1], cube[2]) in cubes:
                n -= 1
        for y in (-1, 1):
            if (cube[0], cube[1] + y, cube[2]) in cubes:
                n -= 1
        for z in (-1, 1):
            if (cube[0], cube[1], cube[2] + z) in cubes:
                n -= 1
    return n


cubes = set()
with open("input.txt") as file:
    for line in file.readlines():
        cubes.add(tuple([int(n) for n in line.strip().split(',')]))

x_min, x_max, y_min, y_max, z_min, z_max = 100000, 0, 100000, 0, 100000, 0
for cube in cubes:
    x_min = min(x_min, cube[0])
    y_min = min(y_min, cube[1])
    z_min = min(z_min, cube[2])
    x_max = max(x_max, cube[0])
    y_max = max(y_max, cube[1])
    z_max = max(z_max, cube[2])

bounding_cube = set()
negative_space = set()
for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):
        for z in range(z_min, z_max + 1):
            cube = (x, y, z)
            bounding_cube.add(cube)
            if cube not in cubes:
                negative_space.add(cube)

bounding_cube_plus_one = set()
for x in range(x_min - 1, x_max + 2):
    for y in range(y_min - 1, y_max + 2):
        for z in range(z_min - 1, z_max + 2):
            cube = (x, y, z)
            bounding_cube_plus_one.add(cube)

print(len(negative_space))
outside_cubes = bounding_cube_plus_one - bounding_cube
while True:
    outside_cubes_next = set()
    for cube in outside_cubes:
        outside_cubes_next.add(cube)
        for x in (-1, 1):
            adjacent_cube = (cube[0] + x, cube[1], cube[2])
            if (x_min <= adjacent_cube[0] <= x_max) and (adjacent_cube not in outside_cubes):
                if adjacent_cube in negative_space:
                    outside_cubes_next.add(adjacent_cube)
                    negative_space.remove(adjacent_cube)
        for y in (-1, 1):
            adjacent_cube = (cube[0], cube[1] + y, cube[2])
            if (y_min <= adjacent_cube[1] <= y_max) and (adjacent_cube not in outside_cubes):
                if adjacent_cube in negative_space:
                    outside_cubes_next.add(adjacent_cube)
                    negative_space.remove(adjacent_cube)
        for z in (-1, 1):
            adjacent_cube = (cube[0], cube[1], cube[2] + z)
            if (z_min <= adjacent_cube[2] <= z_max) and (adjacent_cube not in outside_cubes):
                if adjacent_cube in negative_space:
                    outside_cubes_next.add(adjacent_cube)
                    negative_space.remove(adjacent_cube)
    if len(outside_cubes) == len(outside_cubes_next):
        break
    else:
        outside_cubes = outside_cubes_next

print(len(negative_space))
print(surface_area(cubes) - surface_area(negative_space))