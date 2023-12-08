with open("input_sample.txt") as file:
    lines = file.read()

instructions, network_text = lines.strip().split("\n\n")

network = {}
for line in network_text.split("\n"):
    parts = line.split(" = ")
    left, right = parts[1][1:-1].split(", ")
    network[parts[0]] = (left, right)

cur_node = "AAA"
i, steps = 0, 0
while True:
    cur_node = network[cur_node][0 if instructions[i] == "L" else 1]
    steps += 1
    i += 1
    if i >= len(instructions):
        i = 0
    if cur_node == "ZZZ":
        break

print(steps)
