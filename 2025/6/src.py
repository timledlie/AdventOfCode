import math

with (open("input.txt") as f):
    lines = f.readlines()

numbers = []
for line in lines[:-1]:
    numbers.append([int(n) for n in line.split()])

operations = lines[-1].split()

grand_total = 0
for i in range(len(operations)):
    operands = [n[i] for n in numbers]
    if operations[i] == "+":
        grand_total += sum(operands)
    else:
        grand_total += math.prod(operands)

print(grand_total)
