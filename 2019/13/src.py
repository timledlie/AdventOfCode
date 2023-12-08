# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# from collections import defaultdict
# from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
# import itertools
# import copy
import time

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

        if len(outputs) == 3:
            return outputs


def is_any_machine_still_active(machines: [Machine]):
    for m in machines:
        if not m.is_halted():
            return True
    return False


machine = Machine(memory_orig)
board = [[' ' for y in range(21)] for x in range(38)]


def update_board(board, x, y, tile_id):
    if tile_id == 0:
        board[x][y] = ' '
    elif tile_id == 1:
        board[x][y] = '/'
    elif tile_id == 2:
        board[x][y] = '#'
    elif tile_id == 3:
        board[x][y] = 'O'
    elif tile_id == 4:
        board[x][y] = '$'


ball_x = paddle_x = 0
while True:
    output = intcode_computer(machine, [])
    if len(output) != 3:
        break
    x, y, tile_id = output
    if tile_id == 3:
        paddle_x = x
    elif tile_id == 4:
        ball_x = x
    update_board(board, x, y, tile_id)


def draw_board(board):
    board_string = '\n'.join("".join(board[x][y] for x in range(len(board))) for y in range(len(board[0])))
    print(board_string)
    # return
    # for y in range(len(board[0])):
    #     for x in range(len(board)):
    #         print(board[x][y], sep='', end='')
    #     print()

joystick = 0
while True:
    output = intcode_computer(machine, [joystick])
    if len(output) != 3:
        break
    x, y, tile_id = output
    if x == -1 and y == 0:
        print("SCORE: ", tile_id)
    else:
        update_board(board, x, y, tile_id)
        if tile_id == 4:
            draw_board(board)
            time.sleep(.05)
            ball_x = x
            if ball_x > paddle_x:
                joystick = 1
                paddle_x += 1
            elif ball_x < paddle_x:
                joystick = -1
                paddle_x -= 1
            else:
                joystick = 0
        else:
            joystick = 0