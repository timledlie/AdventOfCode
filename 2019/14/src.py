# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# from collections import defaultdict
from collections import namedtuple
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# from collections import deque
# import re
# import itertools
# import copy

Element = namedtuple('Element', ['name', 'quantity'])
Reaction = namedtuple('Reaction', ['output', 'inputs'])

reactions = {}
with open("input_sample.txt") as file:
    for line in file.readlines():
        inputs, output = line.split(' => ')
        input_elements = []
        for input in inputs.split(', '):
            quantity, input_element_name = input.split()
            input_elements.append(Element(input_element_name, int(quantity)))
        output_quantity, output_name = output.split()
        reactions[output_name] = Reaction(Element(output_name, int(output_quantity)), input_elements)

print(reactions)

elements_needed = reactions['FUEL'].inputs
print(elements_needed)

def is_more_resolution_needed(elements):
    for element in elements:
        if element.name != 'ORE':
            return True
    return False


def merge_ore(elements):
    ret = []
    ore_quantity = 0
    for element in elements:
        if element.name == 'ORE':
            ore_quantity += element.quantity
        else:
            ret.append(element)
    if ore_quantity:
        ret.append(Element('ORE', ore_quantity))
    return ret


while is_more_resolution_needed(elements_needed):
    new_elements_needed = []
    for element in elements_needed:
        if element.name == 'ORE':
            new_elements_needed.append(element)
        else:
            output_needed_name = element.name
            output_needed_quantity = element.quantity
            relevant_reaction = reactions[element.name]

            output_quantity = relevant_reaction.output.quantity
            if output_needed_quantity % output_quantity == 0:
                multiplier = output_needed_quantity // output_quantity
            else:
                multiplier = output_needed_quantity // output_quantity + 1

            for input in relevant_reaction.inputs:
                new_elements_needed.append(Element(input.name, multiplier * input.quantity))
    elements_needed = merge_ore(new_elements_needed)

print(elements_needed)