# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
from collections import defaultdict
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
# from copy import deepcopy

with open("input_sample.txt") as file:
    numbers = [int(c) for c in file.readline().strip().split(',')]

numbers_seen = defaultdict(int)
for i in range(len(numbers) - 1):
    numbers_seen[numbers[i]] = i

n_numbers = len(numbers)
while n_numbers < 30000000:
    ultimate = numbers[-1]
    if ultimate in numbers_seen.keys():
        numbers.append(n_numbers - numbers_seen[ultimate] - 1)
    else:
        numbers.append(0)
    numbers_seen[ultimate] = n_numbers - 1
    n_numbers += 1
print(numbers[-1])