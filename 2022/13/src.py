import copy
from functools import cmp_to_key

divider_packets = [[[2]], [[6]]]
packets = copy.copy(divider_packets)
with open("input.txt") as file:
    for line in file.readlines():
        if line != "\n":
            packets.append(list(eval(line)))


RIGHT = -1
WRONG = 1
UNKNOWN = 0
def in_order(list_a: list, list_b: list):
    for i in range(min(len(list_a), len(list_b))):
        a, b = list_a[i], list_b[i]
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return RIGHT
            elif a > b:
                return WRONG
        else:
            if isinstance(a, int):
                a = [a]
            if isinstance(b, int):
                b = [b]
            result = in_order(a, b)
            if result != UNKNOWN:
                return result

    if len(list_a) < len(list_b):
        return RIGHT
    elif len(list_a) > len(list_b):
        return WRONG
    return UNKNOWN


packets.sort(key=cmp_to_key(in_order))

decoder_key = 1
for i in range(len(packets)):
    if packets[i] in divider_packets:
        decoder_key *= i + 1

print(decoder_key)