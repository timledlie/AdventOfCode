import itertools, math

with (open("input.txt") as f):
    boxes = [tuple(map(int, line.split(','))) for line in f.readlines()]

distances = {}
for a, b in itertools.combinations(boxes, 2):
    distances[(a, b)] = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)

# sort by distance ascending
distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

map_box_to_circuit = {box: i for box, i in list(itertools.zip_longest(boxes, range(len(boxes))))}
map_circuit_to_boxes = {circuit: [box] for box, circuit in map_box_to_circuit.items()}
n_connections = 0
for a, b in distances.keys():
    if map_box_to_circuit[a] != map_box_to_circuit[b]:
        a_circuit, b_circuit = map_box_to_circuit[a], map_box_to_circuit[b]
        map_circuit_to_boxes[a_circuit].extend(map_circuit_to_boxes[b_circuit])
        for box in map_circuit_to_boxes[b_circuit]:
            map_box_to_circuit[box] = a_circuit
        map_circuit_to_boxes[b_circuit] = []
    n_connections += 1
    if n_connections == 1000:
        break

n_boxes_per_circuit = []
for circuit, boxes in map_circuit_to_boxes.items():
    if len(boxes) > 0:
        n_boxes_per_circuit.append(len(boxes))

print(math.prod(sorted(n_boxes_per_circuit, reverse=True)[:3]))
