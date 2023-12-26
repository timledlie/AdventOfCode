with open("input.txt") as file:
    x, y = 0, 0
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    trench = {(x, y)}
    for line in file.readlines():
        parts = line.strip().split()
        direction, count = parts[0], int(parts[1])
        for i in range(count):
            if direction == "U":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "D":
                y += 1
            elif direction == "L":
                x -= 1
            else:
                exit("poop")
            trench.add((x, y))
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)


inside_point = (-47, -232)
# inside_point = (1, 1)

frontier = [inside_point]
while frontier:
    x, y = frontier.pop()
    trench.add((x, y))
    for point in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if point not in trench:
            trench.add(point)
            frontier.append(point)

print(len(trench))
