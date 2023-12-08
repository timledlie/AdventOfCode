# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
import itertools
import copy

with open("input_sample.txt") as file:
    memory_orig = [int(n) for n in file.read().strip().split(',')]


class Machine():
    def __init__(self, memory: list):
        self.memory = memory
        self.pointer = 0

    def is_halted(self):
        return self.memory[self.pointer] == 99


def intcode_computer(machine: Machine, inputs: list):
    outputs = []
    while True:
        pointer = machine.pointer
        memory = machine.memory
        instruction = memory[pointer]
        incr = 2
        jump = None

        if instruction == 99:
            print("graceful termination")
            return outputs

        instruction = str(instruction).zfill(5)
        opcode = instruction[-2:]
        if instruction[2] == '0':
            p1 = memory[memory[pointer + 1]]
        else:
            p1 = memory[pointer + 1]

        if opcode in ('01', '02', '07', '08', '05', '06'):
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
            if (len(inputs) < 1):
                return outputs
            output_index = memory[pointer + 1]
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
        else:
            print("Unexpected opcode", opcode, pointer)
            exit()

        if jump:
            machine.pointer = jump
        else:
            machine.pointer += incr
    return outputs


def is_any_machine_still_active(machines: [Machine]):
    for m in machines:
        if not m.is_halted():
            return True
    return False


max_output_signal = 0
for phase_setting_sequence in itertools.permutations(range(5, 10)):
    machines = [Machine(copy.copy(memory_orig)) for i in range(5)]
    inputs = [[i] for i in list(phase_setting_sequence)]
    inputs[0].append(0)

    while is_any_machine_still_active(machines):
        for i in range(5):
            inputs[(i + 1) % 5] += intcode_computer(machines[i], inputs[i])

    print(phase_setting_sequence, inputs[0][0])
    max_output_signal = max(max_output_signal, inputs[0][0])
print(max_output_signal)