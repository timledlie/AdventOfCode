from collections import defaultdict
from collections import namedtuple

Element = namedtuple('Element', ['name', 'quantity'])
Reaction = namedtuple('Reaction', ['output', 'inputs'])
remainders = defaultdict(int)

reactions = {}
with open("input.txt") as file:
    for line in file.readlines():
        inputs, output = line.split(' => ')
        input_elements = []
        for input in inputs.split(', '):
            quantity, input_element_name = input.split()
            input_elements.append(Element(input_element_name, int(quantity)))
        output_quantity, output_name = output.split()
        reactions[output_name] = Reaction(Element(output_name, int(output_quantity)), input_elements)

elements_needed = reactions['FUEL'].inputs


def is_more_resolution_needed(elements):
    for element in elements:
        if element.name != 'ORE':
            return True
    return False


def merge_elements(elements_dict):
    return [Element(name, quantity) for name, quantity in elements_dict.items()]


while is_more_resolution_needed(elements_needed):
    new_elements_needed = defaultdict(int)
    for element in elements_needed:
        if element.name == 'ORE':
            new_elements_needed[element.name] += element.quantity
        else:
            output_needed_name = element.name
            output_needed_quantity = element.quantity
            if output_needed_quantity <= remainders[output_needed_name]:
                remainders[output_needed_name] -= output_needed_quantity
            else:
                relevant_reaction = reactions[output_needed_name]
                output_quantity = relevant_reaction.output.quantity
                if (output_needed_quantity - remainders[output_needed_name]) % output_quantity == 0:
                    multiplier = (output_needed_quantity - remainders[output_needed_name]) // output_quantity
                else:
                    multiplier = (output_needed_quantity - remainders[output_needed_name]) // output_quantity + 1
                remainders[output_needed_name] += (output_quantity * multiplier) - output_needed_quantity

                for input in relevant_reaction.inputs:
                    new_elements_needed[input.name] += multiplier * input.quantity
    elements_needed = merge_elements(new_elements_needed)

print(elements_needed[0].quantity)
