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

        if len(outputs) == 1:
            return outputs[0]


main_movement_routine = "A,B,A,B,A,C,B,C,A,C"
A = "L,10,L,12,R,6"
B = "R,10,L,4,L,4,L,12"
C = "L,10,R,10,R,6,L,4"

inputs = []
for line in (main_movement_routine, A, B, C):
    for c in line:
        inputs.append(ord(c))
    inputs.append(ord("\n"))
inputs.append(ord("n"))
inputs.append(ord("\n"))

machine = Machine(memory_orig)
while True:
    output = intcode_computer(machine, inputs)
    if not output:
        break
    print(output)
