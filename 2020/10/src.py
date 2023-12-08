# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations

with open("input.txt") as file:
    joltages = [int(line) for line in file.readlines()]

joltages.sort()
print(joltages)
joltages = [0] + joltages + [joltages[-1] + 3]
print(joltages)

product_map = {3: 2, 4: 4, 5: 7, 6:13, 7:24, 8: 44}

i = 0
product = 1
while i < len(joltages) - 1:
    ones_count = 1
    while joltages[i] == joltages[i + 1] - 1:
        i += 1
        ones_count += 1
    i += 1
    if ones_count > 2:
        product *= product_map[ones_count]
print(product)