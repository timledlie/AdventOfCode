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
# from copy import deepcopy

with open("input.txt") as file:
    lines = [l.strip() for l in file.readlines()]

def make_addresses_from_floats(address_with_floats):
    if address_with_floats == '':
        return ['']
    first_char = address_with_floats[0]
    addresses = make_addresses_from_floats(address_with_floats[1:])
    new_addresses = []
    if first_char != 'X':
        for address in addresses:
            new_addresses.append(first_char + address)
    else:
        for address in addresses:
            new_addresses.append('0' + address)
            new_addresses.append('1' + address)
    return new_addresses


memory = {}
for line in lines:
    parts = line.split(" = ")
    if "mask" in line:
        mask = parts[1]
    else:
        value = int(parts[1])
        memory_address = parts[0][4:-1]
        memory_address = "{0:b}".format(int(memory_address))
        memory_address = list(memory_address.zfill(36))
        for i in range(36):
            if mask[i] != '0':
                memory_address[i] = mask[i]
            memory_addresses = make_addresses_from_floats(''.join(memory_address))
        for memory_address in memory_addresses:
            memory[int(memory_address, 2)] = value

sum = 0
for value in memory.values():
    sum += value
print(sum)