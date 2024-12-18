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


def calculate_min_tokens(config):
    big_int = 1000000000000000000
    min_tokens = big_int
    for a_pushes in range(1, 101):
        x1 = a_pushes * config.ax
        y1 = a_pushes * config.ay
        if (x1 > config.prize_x) or (y1 > config.prize_y):
            break
        for b_pushes in range(1, 101):
            x2 = x1 + b_pushes * config.bx
            y2 = y1 + b_pushes * config.by
            if (x2 > config.prize_x) or (y2 > config.prize_y):
                break
            if (x2 == config.prize_x) and (y2 == config.prize_y):
                min_tokens = min(min_tokens, (a_pushes * 3) + b_pushes)

    return 0 if min_tokens == big_int else min_tokens


total_tokens = 0
for config in claw_configs:
    total_tokens += calculate_min_tokens(config)

print(total_tokens)
