from collections import defaultdict
import itertools

graph = defaultdict(set)
with open("input.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

three_sets = set()
for c1 in graph.keys():
    if c1.startswith('t'):
        for c2, c3 in itertools.combinations(graph[c1], 2):
            if c2 in graph[c3]:
                three_sets.add(frozenset((c1, c2, c3)))

print(len(three_sets))
