# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
# from itertools import combinations
# import copy

with open("input.txt") as file:
    memory = [int(n) for n in file.read().strip().split(',')] + [0] * 4000  # padding with 0 simplifies parsing later

print(memory)
pointer = 0
while True:
    instruction = memory[pointer]
    incr = 2
    jump = None

    if instruction == 99:
        print("graceful termination")
        break

    instruction = str(instruction).zfill(5)
    opcode = instruction[-2:]
    pmode1 = instruction[2]
    pmode2 = instruction[1]
    if instruction[2] == '0':
        p1 = memory[memory[pointer + 1]]
    else:
        p1 = memory[pointer + 1]
    if instruction[1] == '0':
        p2 = memory[memory[pointer + 2]]
    else:
        p2 = memory[pointer + 2]

    if opcode in ('01', '02', '07', '08'):
        incr = 4
        output_index = memory[pointer + 3]
        if opcode == '01':
            memory[output_index] = p1 + p2
        elif opcode == '02':
            memory[output_index] = p1 * p2
        elif opcode == '07':
            memory[output_index] = int(p1 < p2)
        elif opcode == '08':
            memory[output_index] = int(p1 == p2)

    elif opcode == '03':
        output_index = memory[pointer + 1]
        memory[output_index] = int(input())
    elif opcode == '04':
        print(p1)
    elif opcode == '05':
        incr = 3
        if p1 != 0:
            jump = p2
    elif opcode == '06':
        incr = 3
        if p1 == 0:
            jump = p2
    else:
        print("Unexpected opcode", opcode, pointer)
        exit()

    if jump:
        pointer = jump
    else:
        pointer += incr
