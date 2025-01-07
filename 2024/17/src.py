with open("input.txt") as file:
    input_text = file.read()

register_text, program_text = input_text.strip().split("\n\n")

parts = register_text.split("\n")
reg_a = int(parts[0][12:])
reg_b = int(parts[1][12:])
reg_c = int(parts[2][12:])

program = [int(c) for c in program_text[9:].split(",")]


def combo(n):
    if 0 <= n <= 3:
        return n
    if n == 4:
        return reg_a
    if n == 5:
        return reg_b
    if n == 6:
        return reg_c
    if n == 7:
        exit("poop")


instruction_pointer = 0
output = []
while instruction_pointer < (len(program) - 1):
    instruction, operand = program[instruction_pointer], program[instruction_pointer + 1]
    is_jump = False

    if instruction == 0:  # adv: division
        reg_a = reg_a // pow(2, combo(operand))
    elif instruction == 1:  # bxl: bitwise XOR
        reg_b = reg_b ^ operand
    elif instruction == 2:  # bst: mod 8
        reg_b = combo(operand) % 8
    elif instruction == 3:  # jnz: jump
        if reg_a != 0:
            instruction_pointer = operand
            is_jump = True
    elif instruction == 4:  # bxc: bitwise XOR
        reg_b = reg_b ^ reg_c
    elif instruction == 5:  # out: output
        output.append(combo(operand) % 8)
    elif instruction == 6:  # bdv: division
        reg_b = reg_a // pow(2, combo(operand))
    elif instruction == 7:  # cdv: division
        reg_c = reg_a // pow(2, combo(operand))

    if not is_jump:
        instruction_pointer += 2

print(",".join([str(c) for c in output]))
