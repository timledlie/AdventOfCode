# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# import math
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
# import copy

with open("input.txt") as file:
    [public_key_1, public_key_2] = [int(line.strip()) for line in file.readlines()]


def get_loop_size(public_key):
    subject_number = 7
    loop_size = 0
    value = 1
    while True:
        loop_size += 1
        value *= subject_number
        value %= 20201227
        if value == public_key:
            return loop_size


def transform(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value


loop_size_1 = get_loop_size(public_key_1)
loop_size_2 = get_loop_size(public_key_2)
private_key_1 = transform(public_key_2, loop_size_1)
private_key_2 = transform(public_key_1, loop_size_2)
print(private_key_1, private_key_2)