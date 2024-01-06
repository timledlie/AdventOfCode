import math

garden_coords, frontier = set(), set()
with open("input.txt") as file:
    lines = file.readlines()
    y_dim = len(lines)
    for y in range(y_dim):
        line = lines[y].strip()
        x_dim = len(line)
        for x in range(x_dim):
            if line[x] == ".":
                garden_coords.add((x, y))
            elif line[x] == "S":
                x_start, y_start = x, y
                frontier = {(x, y)}
                garden_coords.add((x, y))


def same_even_or_odd(a, b):
    return (a % 2) == (b % 2)


def draw_farm(x_min, x_max, y_min, y_max, tracker, step):
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if ((x, y) in tracker) and same_even_or_odd(tracker[(x, y)], step):
                print("O", end="")
            elif (x % x_dim, y % y_dim) in garden_coords:
                print(".", end="")
            else:
                print("#", end="")
        print()
    print()
    print()
    print()


tracker = {(x_start, y_start): 0}
n_steps = 1200
frontier_last = set()
for step in range(1, n_steps + 1):
    frontier_next = set()
    for x, y in frontier:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if ((x + dx) % x_dim, (y + dy) % y_dim) in garden_coords:
                garden_x, garden_y = x + dx, y + dy
                if (garden_x, garden_y) not in frontier_last:
                    frontier_next.add((garden_x, garden_y))
                    tracker[garden_x, garden_y] = step

    frontier_last = frontier
    frontier = frontier_next


n_odds, n_evens = 0, 0
for y in range(y_dim):
    for x in range(x_dim):
        if (x, y) in tracker:
            if tracker[(x, y)] % 2 == 0:
                n_evens += 1
            else:
                n_odds += 1


def n_whole_garden(x_macro, y_macro, steps):
    if ((x_macro + y_macro) % 2) == 0:
        if (steps % 2) == 0:
            return n_evens
        else:
            return n_odds
    else:
        if (steps % 2) == 0:
            return n_odds
        else:
            return n_evens


# for dim = 1, there are 5 squares
def n_whole_garden_times_dim(steps, dim):
    n = n_whole_garden(0, 0, steps)
    multiplier = 4
    for x_macro in range(1, dim + 1):
        n += multiplier * n_whole_garden(x_macro, 0, steps)
        multiplier += 4
    return n


def get_steps_for_coords(x_macro, y_macro, x, y):
    if (x, y) not in tracker:
        return None
    if (abs(x_macro) <= 3) and (abs(y_macro) <= 3):
        return tracker[(x_macro * x_dim + x, y_macro * y_dim + y)]
    if (abs(x_macro) > 3) and (abs(y_macro) > 3):
        exit("invalid input: " + str(x_macro) + ", " + str(y_macro))

    if abs(x_macro) > 3:
        x_sign = 1 if x_macro >= 0 else -1
        baseline = tracker[(x_sign * 3 * x_dim + x, y_macro * y_dim + y)]
        bump = (abs(x_macro) - 3) * x_dim
        return baseline + bump

    if abs(y_macro) > 3:
        y_sign = 1 if y_macro >= 0 else -1
        baseline = tracker[(x_macro * x_dim + x, y_sign * 3 * y_dim + y)]
        bump = (abs(y_macro) - 3) * y_dim
        return baseline + bump


def count_macro_coords(x_macro_target, y_macro_target, steps):
    count_partial_garden = 0
    for x, y in garden_coords:
        projected_steps = get_steps_for_coords(x_macro_target, y_macro_target, x, y)
        if (projected_steps is not None) and (projected_steps <= steps) and (same_even_or_odd(projected_steps, steps)):
            count_partial_garden += 1

    return count_partial_garden, n_whole_garden(x_macro_target, y_macro_target, steps)


steps = 26501365
max_distance = math.ceil(steps / x_dim)
count_gardens = 0
for x_macro in range(max_distance, max_distance - 4, -1):
    count_gardens += count_macro_coords(x_macro, 0, steps)[0]
    count_gardens += abs(x_macro) * count_macro_coords(x_macro, 1, steps)[0]
count_gardens -= count_macro_coords(x_macro, 0, steps)[0]

for y_macro in range(max_distance, max_distance - 4, -1):
    count_gardens += count_macro_coords(0, y_macro, steps)[0]
    count_gardens += abs(y_macro) * count_macro_coords(-1, y_macro, steps)[0]
count_gardens -= count_macro_coords(0, y_macro, steps)[0]

for x_macro in range(-max_distance, -max_distance + 4, 1):
    count_gardens += count_macro_coords(x_macro, 0, steps)[0]
    count_gardens += abs(x_macro) * count_macro_coords(x_macro, -1, steps)[0]
count_gardens -= count_macro_coords(x_macro, 0, steps)[0]

for y_macro in range(-max_distance, -max_distance + 4, 1):
    count_gardens += count_macro_coords(0, y_macro, steps)[0]
    count_gardens += abs(y_macro) * count_macro_coords(1, y_macro, steps)[0]
count_gardens -= count_macro_coords(0, y_macro, steps)[0]

count_gardens += n_whole_garden_times_dim(steps, max_distance - 3)

print(count_gardens)
