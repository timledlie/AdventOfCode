obstructions = set()
start_x, start_y = None, None
start_dir = "up"
y = 0
with open("input.txt") as file:
    for line in file.readlines():
        x = 0
        line = line.strip()
        for char in line:
            if char == "#":
                obstructions.add((x, y))
            elif char == "^":
                start_x, start_y = x, y
            x += 1
        y += 1
max_x, max_y = x - 1, y - 1


def is_loop_in_walk(cur_x, cur_y, cur_dir, obstructions):
    locations_visited = set()
    while (0 <= cur_x <= max_x) and (0 <= cur_y <= max_y):
        if (cur_x, cur_y, cur_dir) in locations_visited:
            return True

        locations_visited.add((cur_x, cur_y, cur_dir))

        if cur_dir == "up":
            if (cur_x, cur_y - 1) in obstructions:
                cur_dir = "right"
            else:
                cur_y -= 1
        elif cur_dir == "right":
            if (cur_x + 1, cur_y) in obstructions:
                cur_dir = "down"
            else:
                cur_x += 1
        elif cur_dir == "down":
            if (cur_x, cur_y + 1) in obstructions:
                cur_dir = "left"
            else:
                cur_y += 1
        elif cur_dir == "left":
            if (cur_x - 1, cur_y) in obstructions:
                cur_dir = "up"
            else:
                cur_x -= 1
    
    return False


loop_count = 0
for x in range(max_x + 1):
    for y in range(max_y + 1):
        if (x, y) not in obstructions:
            if is_loop_in_walk(start_x, start_y, start_dir, obstructions.union({(x, y)})):
                loop_count += 1

print(loop_count)
