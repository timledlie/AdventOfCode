from collections import defaultdict

graph = defaultdict(set)
with open("input.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)

max_cliques = []


# From https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm#Without_pivoting
def bron_kerbosch(r, p, x):
    if len(p) == 0 and len(x) == 0:
        max_cliques.append(r)
        return
    for v in p:
        bron_kerbosch(r | {v}, p & graph[v], x & graph[v])
        p = p - {v}
        x = x | {v}


bron_kerbosch(set(), set(graph.keys()), set())

print(','.join(sorted(max(max_cliques, key=len))))
