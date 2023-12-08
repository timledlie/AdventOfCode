# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
# import itertools
# import copy

with open("input.txt") as file:
    memory_orig = [int(n) for n in file.read().strip().split(',')] + [0] * 4000


class Machine():
    def __init__(self, memory: list):
        self.memory = memory
        self.pointer = 0
        self.relative_base = 0

    def is_halted(self):
        return self.memory[self.pointer] == 99


def intcode_computer(machine: Machine, inputs: list):
    outputs = []
    while True:
        pointer = machine.pointer
        memory = machine.memory
        instruction = memory[pointer]
        # print(instruction)
        incr = 2
        jump = None

        if instruction == 99:
            print("graceful termination")
            return outputs

        instruction = str(instruction).zfill(5)
        opcode = instruction[-2:]
        if instruction[2] == '0':
            p1 = memory[memory[pointer + 1]]
        elif instruction[2] == '1':
            p1 = memory[pointer + 1]
        else:
            p1 = memory[machine.relative_base + memory[pointer + 1]]

        if opcode in ('01', '02', '07', '08', '05', '06'):
            if instruction[1] == '0':
                p2 = memory[memory[pointer + 2]]
            elif instruction[1] == '1':
                p2 = memory[pointer + 2]
            else:
                p2 = memory[machine.relative_base + memory[pointer + 2]]

        if opcode in ('01', '02', '07', '08'):
            incr = 4
            if instruction[0] == '0':
                output_index = memory[pointer + 3]
            elif instruction[0] == '1':
                print("Unexpected input situation", opcode, pointer)
            else:
                output_index = machine.relative_base + memory[pointer + 3]
            # output_index = memory[pointer + 3]
            if opcode == '01':
                memory[output_index] = p1 + p2
            elif opcode == '02':
                memory[output_index] = p1 * p2
            elif opcode == '07':
                memory[output_index] = int(p1 < p2)
            elif opcode == '08':
                memory[output_index] = int(p1 == p2)

        elif opcode == '03':
            if (len(inputs) < 1):
                return outputs
            if instruction[2] == '0':
                output_index = memory[pointer + 1]
            elif instruction[2] == '1':
                print("Unexpected input situation", opcode, pointer)
            else:
                output_index = machine.relative_base + memory[pointer + 1]
            memory[output_index] = inputs.pop(0)
        elif opcode == '04':
            outputs.append(p1)
        elif opcode == '05':
            incr = 3
            if p1 != 0:
                jump = p2
        elif opcode == '06':
            incr = 3
            if p1 == 0:
                jump = p2
        elif opcode == '09':
            incr = 2
            machine.relative_base += p1
        else:
            print("Unexpected opcode", opcode, pointer)
            exit()

        if jump is not None:
            machine.pointer = jump
        else:
            machine.pointer += incr

        if len(outputs) == 2:
            return outputs


def is_any_machine_still_active(machines: [Machine]):
    for m in machines:
        if not m.is_halted():
            return True
    return False


machine = Machine(memory_orig)

robot_position = [0, 0]
robot_orientation = 'up'
colored_panels = {(0, 0): 1}
while True:
    if tuple(robot_position) in colored_panels.keys():
        current_panel_color = colored_panels[tuple(robot_position)]
    else:
        current_panel_color = 0

    output = intcode_computer(machine, [current_panel_color])
    if len(output) != 2:
        break
    color, turn_direction = output

    colored_panels[tuple(robot_position)] = color

    if turn_direction == 0:  # turn left
        if robot_orientation == 'up':
            robot_orientation = 'left'
        elif robot_orientation == 'right':
            robot_orientation = 'up'
        elif robot_orientation == 'down':
            robot_orientation = 'right'
        elif robot_orientation == 'left':
            robot_orientation = 'down'
    elif turn_direction == 1:  # turn right
        if robot_orientation == 'up':
            robot_orientation = 'right'
        elif robot_orientation == 'right':
            robot_orientation = 'down'
        elif robot_orientation == 'down':
            robot_orientation = 'left'
        elif robot_orientation == 'left':
            robot_orientation = 'up'
    else:
        exit('Poop')

    if robot_orientation == 'up':
        robot_position[1] += 1
    elif robot_orientation == 'right':
        robot_position[0] += 1
    elif robot_orientation == 'down':
        robot_position[1] -= 1
    elif robot_orientation == 'left':
        robot_position[0] -= 1


print(len(colored_panels))
min_x = max_x = min_y = max_y = 0
for position, color in colored_panels.items():
    if color == 1:
        min_x = min(min_x, position[0])
        max_x = max(max_x, position[0])
        min_y = min(min_y, position[1])
        max_y = max(max_y, position[1])
print(min_x, max_x, min_y, max_y)

for y in range(max_y, min_y - 1, -1):
    for x in range(min_x, max_x + 1):
        if (x, y) in colored_panels:
            if colored_panels[(x, y)] == 1:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        else:
            print(' ', end=' ')

    print()