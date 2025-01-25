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
    exit("poop")


wires_with_values = set(wire_values.keys())
wires_without_values = all_wires - wires_with_values
while len(wires_without_values) > 0:
    without_next = set()
    for wire in wires_without_values:
        gate = gates[wire]
        if (gate.inputs[0] in wires_with_values) and (gate.inputs[1] in wires_with_values):
            output = calculate_output(gate.type, wire_values[gate.inputs[0]], wire_values[gate.inputs[1]])
            wire_values[wire] = output
            wires_with_values.add(wire)
        else:
            without_next.add(wire)
    wires_without_values = without_next

print(int(''.join([str(int(wire_values[wire])) for wire in sorted([wire for wire in all_wires if wire.startswith('z')], reverse=True)]), 2))
