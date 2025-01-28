from collections import namedtuple

Gate = namedtuple("Gate", ["type", "inputs", "output"])

with open("input.txt") as file:
    text_data = file.read()
    starting_values_text, gates_text = text_data.strip().split("\n\n")

wire_values = {}
for line in starting_values_text.split("\n"):
    wire, value = line.split(": ")
    wire_values[wire] = bool(int(value))

gates = {}
all_wires = set()
for line in gates_text.split("\n"):
    inputs, output = line.split(" -> ")
    input1, gate_type, input2 = inputs.split(" ")
    gates[output] = Gate(gate_type, (input1, input2), output)
    all_wires.update((input1, input2, output))


def calculate_output(operation, a, b):
    if operation == "AND":
        return a and b
    if operation == "OR":
        return a or b
    if operation == "XOR":
        return a != b


def print_gate(g: Gate):
    print(g.inputs[0], g.type, g.inputs[1], "->", g.output)


def print_recursive(wire):
    if wire.startswith(('x', 'y')):
        print(wire, sep='', end='')
    else:
        print(wire, ": (", sep='', end='')
        gate = gates[wire]
        if (gate.inputs[0].startswith(('x','y'))) or gates[gate.inputs[0]].inputs[0].startswith(('x', 'y')):
            in1, in2 = gate.inputs[0], gate.inputs[1]
        else:
            in1, in2 = gate.inputs[1], gate.inputs[0]
        print_recursive(in1)
        print(" ", gate.type, " ", sep='', end='')
        print_recursive(in2)
        print(")", sep='', end='')


def swap_gate_outputs(a, b):
    gate_a, gate_b = gates[a], gates[b]
    gate_a_new = Gate(gate_b.type, gate_b.inputs, a)
    gate_b_new = Gate(gate_a.type, gate_a.inputs, b)
    gates[a] = gate_a_new
    gates[b] = gate_b_new


swap_gate_outputs('z19', 'sbg')
swap_gate_outputs('z12', 'djg')
swap_gate_outputs('hjm', 'mcq')
swap_gate_outputs('dsd', 'z37')
# for z_wire in sorted([wire for wire in all_wires if wire.startswith('z')]):
#     print_recursive(z_wire)
#     print()
# exit()

for wire in all_wires:
    if wire.startswith(('x', 'y')):
        wire_values[wire] = True

wires_with_values = set(wire_values.keys())
wires_without_values = all_wires - wires_with_values
while len(wires_without_values) > 0:
    without_next = set()
    n_changes = 0
    for wire in wires_without_values:
        gate = gates[wire]
        if (gate.inputs[0] in wires_with_values) and (gate.inputs[1] in wires_with_values):
            output = calculate_output(gate.type, wire_values[gate.inputs[0]], wire_values[gate.inputs[1]])
            wire_values[wire] = output
            wires_with_values.add(wire)
            n_changes += 1
        else:
            without_next.add(wire)
    wires_without_values = without_next

print(''.join([str(int(wire_values[wire])) for wire in sorted([wire for wire in all_wires if wire.startswith('z')], reverse=True)]))
