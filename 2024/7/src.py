from collections import namedtuple

Equation = namedtuple('Equation', ['test_value', 'numbers'])
equations = []
with open("input.txt") as file:
    for line in file.readlines():
        test_value, numbers = line.strip().split(": ")
        equations.append(Equation(int(test_value), [int(n) for n in numbers.split()]))


def is_solvable(equation):
    running_possible_values = [equation.numbers.pop(0)]
    while len(equation.numbers) > 0:
        next_number = equation.numbers.pop(0)
        next_possible_values = []
        for value in running_possible_values:
            next_value = value + next_number
            if next_value == equation.test_value:
                return True
            if next_value < equation.test_value:
                next_possible_values.append(next_value)

            next_value = value * next_number
            if next_value == equation.test_value:
                return True
            if next_value < equation.test_value:
                next_possible_values.append(next_value)
        running_possible_values = next_possible_values
    return False


total_calibration_result = 0
for equation in equations:
    if is_solvable(equation):
        total_calibration_result += equation.test_value

print(total_calibration_result)
