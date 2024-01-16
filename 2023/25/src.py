from collections import defaultdict
import random
import copy

graph = defaultdict(list)
with open("input.txt") as file:
    for line in file.readlines():
        from_node, to_nodes = line.strip().split(": ")
        to_nodes = to_nodes.split(" ")
        for to_node in to_nodes:
            if to_node not in graph[from_node]:
                graph[from_node].append(to_node)
            if from_node not in graph[to_node]:
                graph[to_node].append(from_node)

super_nodes = {}
for node in graph.keys():
    super_nodes[node] = {node}

super_nodes_original = copy.deepcopy(super_nodes)
graph_original = copy.deepcopy(graph)
# Krager's algorithm for minimum cut, taken from:
# https://web.stanford.edu/class/archive/cs/cs161/cs161.1172/CS161Lecture16.pdf
# https://medium.com/@dev.elect.iitd/kargers-algorithm-d8067eb1b790 and
while True:
    super_nodes = copy.deepcopy(super_nodes_original)
    graph = copy.deepcopy(graph_original)
    while len(graph.keys()) > 2:
        n1 = random.choice(list(graph.keys()))
        n2 = random.choice(graph[n1])

        graph[n1].extend(graph[n2])
        for node in graph[n2]:
            graph[node].remove(n2)
            graph[node].append(n1)
        while n1 in graph[n1]:
            graph[n1].remove(n1)
        del graph[n2]

        super_nodes[n1].update(super_nodes[n2])
        del super_nodes[n2]
    if len(graph[list(graph.keys())[0]]) == 3:
        sn_keys = list(super_nodes.keys())
        print(len(super_nodes[sn_keys[0]]) * len(super_nodes[sn_keys[1]]))
        break
