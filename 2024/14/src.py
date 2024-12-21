class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return " ".join([str(v) for v in (self.x, self.y, self.vx, self.vy)])


robots = []
with open("input.txt") as file:
    for line in file.readlines():
        position_text, velocity_text = line.split(" ")
        x, y = tuple([int(pos) for pos in position_text[2:].split(",")])
        vx, vy = tuple([int(vel) for vel in velocity_text[2:].split(",")])
        robots.append(Robot(x, y, vx, vy))

# x_dim, y_dim = 11, 7
x_dim, y_dim = 101, 103

for second in range(100):
    for robot in robots:
        robot.x = (robot.x + robot.vx) % x_dim
        robot.y = (robot.y + robot.vy) % y_dim

n_q1, n_q2, n_q3, n_q4 = 0, 0, 0, 0
x_mid, y_mid = x_dim // 2, y_dim // 2
for robot in robots:
    if robot.x < x_mid:
        if robot.y < y_mid:
            n_q1 += 1
        elif robot.y > y_mid:
            n_q3 += 1
    elif robot.x > x_mid:
        if robot.y < y_mid:
            n_q2 += 1
        elif robot.y > y_mid:
            n_q4 += 1

print(n_q1 * n_q2 * n_q3 * n_q4)
