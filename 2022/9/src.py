motions = []
with open("input.txt") as file:
    for line in file.readlines():
        direction, steps = line.strip().split()
        motions += direction * int(steps)

n_knots = 10
knots = [[0, 0] for i in range(n_knots)]
tail_visited = {tuple(knots[n_knots - 1])}


def move_head(m, knots):
    if m == "U":
        knots[0][1] += 1
    elif m == "D":
        knots[0][1] -= 1
    elif m == "L":
        knots[0][0] -= 1
    elif m == "R":
        knots[0][0] += 1


def update_trailing_knot(knots, i, j):
    x_distance = knots[i][0] - knots[j][0]
    y_distance = knots[i][1] - knots[j][1]
    if abs(x_distance) == 2 and y_distance == 0:
        knots[j][0] += x_distance // abs(x_distance)
    elif abs(y_distance) == 2 and x_distance == 0:
        knots[j][1] += y_distance // abs(y_distance)
    elif abs(x_distance) == 2 or abs(y_distance) == 2:
        knots[j][0] += x_distance // abs(x_distance)
        knots[j][1] += y_distance // abs(y_distance)


def draw_knots(knots):
    window = 7
    knot_positions = {}
    for i in range(n_knots):
        knot_positions[tuple(knots[i])] = i

    for y in range(window, -1 * window, -1):
        for x in range(-1 * window, window):
            if (x, y) in knot_positions:
                print(knot_positions[(x, y)], end='')
            else:
                print(".", end='')
        print()
    print()


for m in motions:
    move_head(m, knots)
    for i, j in zip(range(n_knots - 1), range(1, n_knots)):
        update_trailing_knot(knots, i, j)
    tail_visited.add(tuple(knots[n_knots - 1]))
    # draw_knots(knots)

print(len(tail_visited))
