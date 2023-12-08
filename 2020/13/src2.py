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
    bus_id_string = file.readline().strip()
    bus_ids_dict = {}
    bus_ids_list = []
    bus_ids_tuples = []
    index = 0
    for bus_id in bus_id_string.split(','):
        bus_ids_list.append(bus_id)
        if bus_id != 'x':
            bus_ids_dict[index] = int(bus_id)
            bus_ids_tuples.append((index, int(bus_id)))
        index += 1
print(bus_ids_dict)
print(bus_ids_list)
print(bus_ids_tuples)

tuple1 = bus_ids_tuples.pop(0)
tuple2 = bus_ids_tuples.pop(0)
start = 0
period = tuple1[1]
gap = tuple2[0]
target = tuple2[1]
while True:
    if (start + gap) % target == 0:
        break
    start += period
period *= tuple2[1]

while bus_ids_tuples:
    bus_id_tuple = bus_ids_tuples.pop(0)
    gap = bus_id_tuple[0]
    target = bus_id_tuple[1]
    while True:
        if (start + gap) % target == 0:
            break
        start += period
    period *= bus_id_tuple[1]

print(start)