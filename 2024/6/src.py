obstructions = set()
cur_x, cur_y = None, None
cur_direction = "up"
y = 0
with open("input.txt") as file:
    for line in file.readlines():
        x = 0
        line = line.strip()
        for char in line:
            if char == "#":
                obstructions.add((x, y))
            elif char == "^":
                cur_x, cur_y = x, y
            x += 1
        y += 1
max_x, max_y = x - 1, y - 1

locations_visited = set()
while (0 <= cur_x <= max_x) and (0 <= cur_y <= max_y):
    locations_visited.add((cur_x, cur_y))
    if cur_direction == "up":
        if (cur_x, cur_y - 1) in obstructions:
            cur_direction = "right"
        else:
            cur_y -= 1
    elif cur_direction == "right":
        if (cur_x + 1, cur_y) in obstructions:
            cur_direction = "down"
        else:
            cur_x += 1
    elif cur_direction == "down":
        if (cur_x, cur_y + 1) in obstructions:
            cur_direction = "left"
        else:
            cur_y += 1
    elif cur_direction == "left":
        if (cur_x - 1, cur_y) in obstructions:
            cur_direction = "up"
        else:
            cur_x -= 1

print(len(locations_visited))
