import functools

graph = {}
with (open("input.txt") as f):
    for line in f.readlines():
        input_node, output_nodes = line.split(':')
        graph[input_node] = [node for node in output_nodes.strip().split()]

@functools.cache
def count_paths(node, has_visited_dac, has_visited_fft):
    if node == "out":
        return int(has_visited_dac and has_visited_fft)

    if node == "dac":
        has_visited_dac = True
    if node == "fft":
        has_visited_fft = True

    return sum([count_paths(node, has_visited_dac, has_visited_fft) for node in graph[node]])

print(count_paths("svr", False, False))
