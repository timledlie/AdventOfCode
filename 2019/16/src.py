# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
# import itertools
# import copy

with open("input.txt") as file:
    signal = [int(el) for el in list(file.readline().strip())]


def make_pattern(n):
    if n == 1:
        return (1, 1), (0, 1), (-1, 1), (0, 1)
    return (0, n - 1), (1, n), (0, n), (-1, n), (0, 1)


print(make_pattern(1))
print(make_pattern(2))
print(make_pattern(3))
print(make_pattern(4))
print(make_pattern(5))
exit()

length_multiplier = 1
for phase in range(1, 101):
    signal_next = []
    for n in range(1, len(signal) + 1):
        pattern = make_pattern(n)
        print(pattern)
        sum = n_chars = 0
        signal_index = pattern_index = 0

        while n_chars < len(signal) * length_multiplier:
            sum += signal[signal_index] * pattern[pattern_index]
            n_chars += 1
            signal_index += 1
            if signal_index == len(signal):
                signal_index = 0
            pattern_index += 1
            if pattern_index == len(pattern):
                pattern_index = 0

        signal_next.append(abs(sum) % 10)

    signal = signal_next
    print("After", phase, "phase:", ''.join(str(i) for i in signal[:8]))