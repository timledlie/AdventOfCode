cave = set()
with open("input.txt") as file:
    for line in file.readlines():
        points = line.split(" -> ")
        [x_start, y_start] = [int(n) for n in points[0].split(',')]
        for point in points[1:]:
            [x_end, y_end] = [int(n) for n in point.split(',')]
            if x_start != x_end:
                for x in range(min(x_start, x_end), max(x_start, x_end) + 1):
                    cave.add((x, y_start))
            else:
                for y in range(min(y_start, y_end), max(y_start, y_end) + 1):
                    cave.add((x_start, y))
            x_start, y_start = x_end, y_end

x_min, x_max, y_max = 1000000, 0, 0
y_min = 0
for x, y in cave:
    x_min = min(x_min, x)
    x_max = max(x_max, x)
    y_max = max(y_max, y)

print(x_min, x_max, 0, y_max)
y_max += 2
for x in range(x_min - 300, x_max + 300):
    cave.add((x, y_max))


def print_cave(cave, sand, x_min, x_max, y_max):
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in cave:
                char = '#'
            elif (x, y) in sand:
                char = 'o'
            elif (x, y) == (500, 0):
                char = '+'
            else:
                char = '.'
            print(char, sep='', end='')
        print()
    print()


def simulate_grain_fall(cave, sand, y_max):
    x_sand, y_sand = 500, 0
    while True:
        if y_sand > y_max:
            break
        below = (x_sand, y_sand + 1)
        below_left = (x_sand - 1, y_sand + 1)
        below_right = (x_sand + 1, y_sand + 1)
        if below not in cave and below not in sand:
            y_sand += 1
        elif below_left not in cave and below_left not in sand:
            x_sand -= 1
            y_sand += 1
        elif below_right not in cave and below_right not in sand:
            x_sand += 1
            y_sand += 1
        else:
            sand.add((x_sand, y_sand))
            if (x_sand, y_sand) == (500, 0):
                break
            x_sand, y_sand = 500, 0
            # print(len(sand))
            # print_cave(cave, sand, x_min - 20, x_max + 20, y_max)


sand = set()
simulate_grain_fall(cave, sand, y_max)
print(len(sand))