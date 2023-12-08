# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
# from copy import deepcopy
import ast

with open("input.txt") as file:
    lines = ['(' + line.strip() + ')' for line in file.readlines()]


def expression_value(expression):
    first_element = expression.pop(0)
    if type(first_element) is list:
        value = expression_value(first_element)
    else:
        value = first_element

    if len(expression) == 0:
        return value

    while len(expression) > 0:
        operation = expression.pop(0)
        if operation == '+':
            next_expression = expression.pop(0)
            if type(next_expression) is list:
                next_value = expression_value(next_expression)
            else:
                next_value = next_expression
            value = value + next_value
        elif operation == '*':
            next_value = expression_value(expression)
            value = value * next_value

    return value


def convert_to_list(expression):
    expression = expression.replace(' ', ', ')
    expression = expression.replace("+", "'+'")
    expression = expression.replace("*", "'*'")
    expression = expression.replace("(", "[")
    expression = expression.replace(")", "]")
    return ast.literal_eval(expression)

sum = 0
for line in lines:
    value = expression_value(convert_to_list(line))
    print(value, line)
    sum += value
print(sum)