# import statistics
from collections import deque
# import math
# import json

with open("input.txt") as file:
    chars = file.read().strip()

n = 14
d = deque(chars[:n], n)
while len(d) != len(set(d)):
    d.append(chars[n])
    n += 1
print(n)