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

def find_common_root(bus_ids_list, bus_ids_inv, multiplier):
    bus_a_id = bus_ids_list[0]
    bus_b_id = bus_ids_list[1]
    bus_a_offset = bus_ids_inv[bus_a_id]
    bus_b_offset = bus_ids_inv[bus_b_id]
    ab = bus_a_id * bus_b_id * multiplier
    for n in range(ab, 1, -1 * bus_a_id):
        if (n + bus_b_offset - bus_a_offset) % bus_b_id == 0:
            return n - bus_a_offset


with open("input_sample.txt") as file:
    bus_id_string = file.readline().strip()
    bus_ids_dict = {}
    bus_ids_list = []
    index = 0
    for bus_id in bus_id_string.split(','):
        bus_ids_list.append(bus_id)
        if bus_id != 'x':
            bus_ids_dict[index] = int(bus_id)
        index += 1
print(bus_ids_dict)
print(bus_ids_list)

print('{0: >5}'.format("time"), end='')
for bus_id in bus_ids_list:
    print('{0: >5}'.format(bus_id), end='')
print()

for i in range(250):
    print('{0: >5}'.format(str(i)), end='')
    for offset, bus_id in enumerate(bus_ids_list):
        if bus_id == 'x':
            print('{0: >5}'.format('.'), end='')
        else:
            if i % int(bus_id) == 0:
                print('{0: >5}'.format('D'), end='')
            else:
                print('{0: >5}'.format('.'), end='')
    print()
exit()

# bus_ids_inv = {v: k for k, v in bus_ids.items()}
# print(bus_ids_inv)
# bus_ids_list = list(bus_ids_inv.keys())
# bus_ids_list.sort(reverse=True)
# print(bus_ids_list)
# product = 1
# for bus_id in bus_ids_list[:-1]:
#     product *= bus_id

multiplier = product
while True:
    common_root = find_common_root(bus_ids_list, bus_ids_inv, multiplier)
    is_all_divisible = True
    for bus_id in bus_ids_list[2:]:
        diff = bus_ids_inv[bus_id]
        if (common_root + diff) % bus_id != 0:
            is_all_divisible = False
            break
    if is_all_divisible:
        print(common_root)
        exit()
    multiplier -= 1