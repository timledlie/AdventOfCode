graph = {}
with (open("input.txt") as f):
    for line in f.readlines():
        input_node, output_nodes = line.split(':')
        graph[input_node] = [node for node in output_nodes.strip().split()]

def count_paths(graph, node):
    if node == "out":
        return 1

    return sum([count_paths(graph, node) for node in graph[node]])

print(count_paths(graph, "you"))
