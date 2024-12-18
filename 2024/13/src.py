from collections import namedtuple
import re

ClawConfig = namedtuple("ClawConfig", ["ax", "ay", "bx", "by", "prize_x", "prize_y"])

with open("input.txt") as file:
    input_text = file.read()
    scenarios = input_text.strip().split("\n\n")

p = re.compile(r"Button A: X\+(\d+), Y\+(\d+).*Button B: X\+(\d+), Y\+(\d+).*Prize: X=(\d+), Y=(\d+)", re.DOTALL)

claw_configs = []
for scenario in scenarios:
    m = p.search(scenario)
    claw_configs.append(ClawConfig(*[int(g) for g in m.groups()]))


def calculate_min_tokens(c, err):
    # two equations with two unknowns
    d = c.bx * (c.prize_y + err) - c.by * (c.prize_x + err)
    e = c.ay * c.bx - c.ax * c.by
    f = c.ax * (c.prize_y + err) - c.ay * (c.prize_x + err)
    g = c.ax * c.by - c.ay * c.bx
    # must be evenly divisible
    if ((d % e) == 0) and ((f % g) == 0):
        h = d // e
        i = f // g
        if (h > 0) and (i > 0):
            return (3 * h) + i
    return 0


total_tokens = 0
for config in claw_configs:
    total_tokens += calculate_min_tokens(config, 10000000000000)

print(total_tokens)
