# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# import math
# import json
# import copy
import random

instructions = []
with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        instructions.append(line.split())
print(instructions)


def calc_z(input_values):
    reg = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in instructions:
        command = i[0]
        a = i[1]
        if command == "inp":
            reg[a] = int(input_values.pop(0))
        else:
            b = i[2]
            if b[0] == '-' or b.isnumeric():
                b = int(b)
            else:
                b = reg[b]
            if command == "add":
                reg[a] += b
            elif command == "mul":
                reg[a] *= b
            elif command == "div":
                reg[a] = reg[a] // b
            elif command == "mod":
                reg[a] = reg[a] % b
            elif command == "eql":
                reg[a] = int(reg[a] == b)
    if reg['z'] == 0:
        return True
    return False


def generate_input():
    # 99691691779938
    # 01234567890123
    #                0    1    2    3    4    5    6    7    8    9    0    1    2    3
    #                a    b    c    d    e    f    g    h    i    j    k    l    m    n
    random_input = ['9', '9', '0', '0', '0', '0', '9', '1', '0', '0', '0', '0', '0', '0']

    random_input[0] = '2'
    random_input[1] = '7'
    random_input[2] = '1'

    random_input[3] = str(int(random_input[2]) + 3)

    random_input[4] = str(random.randint(1, 9))
    random_input[5] = str(random.randint(1, 8))
    random_input[8] = str(int(random_input[5]) + 1)
    random_input[9] = str(random.randint(1, 7))
    random_input[10] = str(int(random_input[9]) + 2)
    random_input[11] = str(random.randint(1, 9))
    random_input[12] = str(random.randint(1, 9))
    random_input[13] = str(random.randint(1, 9))
    return random_input

# minimum = pow(10, 13)
# maximum = 99691891946938
winners = set()
minimum = 28691291324921
while True:
    random_input = generate_input()
    if int(''.join(random_input)) >= minimum:
        continue
    random_input_copy = random_input.copy()
    if calc_z(random_input):
        yep = int(''.join(random_input_copy))
        winners.add(yep)
        minimum = min(winners)
        print("Added", f'{yep:>14}', "now we have", f'{len(winners):>3}', "min is", f'{min(winners):>14}')
