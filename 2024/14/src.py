class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return " ".join([str(v) for v in (self.x, self.y, self.vx, self.vy)])


points_inside_tree = set()
for y in range(101):
    for x_delta in range(-(y // 2), (y // 2) + 1):
        points_inside_tree.add((50 + x_delta, y))

robots = []
with open("input.txt") as file:
    for line in file.readlines():
        position_text, velocity_text = line.split(" ")
        x, y = tuple([int(pos) for pos in position_text[2:].split(",")])
        vx, vy = tuple([int(vel) for vel in velocity_text[2:].split(",")])
        robots.append(Robot(x, y, vx, vy))

x_dim, y_dim = 101, 103

max_second, max_inside_tree = None, 0
for second in range(x_dim * y_dim):
    n_in_tree = 0
    for robot in robots:
        robot.x = (robot.x + robot.vx) % x_dim
        robot.y = (robot.y + robot.vy) % y_dim
        if (robot.x, robot.y) in points_inside_tree:
            n_in_tree += 1
    if n_in_tree > max_inside_tree:
        max_second = second + 1
        max_inside_tree = n_in_tree

print(max_second)
