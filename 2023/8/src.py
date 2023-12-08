import numpy

with open("input.txt") as file:
    lines = file.read()


def get_end_steps_from_node(start_node, instructions, network, end_nodes):
    cur_node = start_node
    end_steps = []
    i, steps = 0, 0
    network_traversing_states = set((i, cur_node))
    while True:
        cur_node = network[cur_node][0 if instructions[i] == "L" else 1]
        i += 1
        steps += 1
        if cur_node in end_nodes:
            end_steps.append(steps)
        if (i, cur_node) in network_traversing_states:
            return end_steps
        else:
            network_traversing_states.add((i, cur_node))
        if i >= len(instructions):
            i = 0


instructions, network_text = lines.strip().split("\n\n")

network = {}
start_nodes, end_nodes = set(), set()
for line in network_text.split("\n"):
    parts = line.split(" = ")
    origin = parts[0]
    left, right = parts[1][1:-1].split(", ")

    if origin[-1] == "A":
        start_nodes.add(origin)

    if left[-1] == "Z":
        end_nodes.add(left)

    if right[-1] == "Z":
        end_nodes.add(right)

    network[origin] = (left, right)

end_steps_from_start = {}
for start_node in start_nodes:
    end_steps_from_start[start_node] = get_end_steps_from_node(start_node, instructions, network, end_nodes)

print(end_steps_from_start)
endpoints = []
for end_steps in end_steps_from_start.values():
    endpoints += end_steps

print(numpy.lcm.reduce(endpoints))
