import re
import datetime

flow_rates = {}
graph = {}
with open("input.txt") as file:
    for line in file.readlines():
        m = re.search('Valve (.+?) has flow rate=(.+?); tunnel[s]* lead[s]* to valve[s]* (.+?)\n', line)

        valve = m.group(1)
        flow_rate = int(m.group(2))
        connected_valves = m.group(3).split(', ')

        flow_rates[valve] = flow_rate
        graph[valve] = connected_valves

valves = flow_rates.keys()


def min_distance(a, b, visited):
    if b in graph[a]:
        return 1
    visited = visited + (a,)
    min_dist = 100000
    for node in graph[a]:
        if node not in visited:
            min_dist = min(min_dist, min_distance(node, b, visited))
    return 1 + min_dist


distances = {}
all_valves = list(flow_rates.keys())
all_valves.sort(key=lambda valve: flow_rates[valve], reverse=True)
for i in range(len(all_valves) - 1):
    for j in range(i + 1, len(all_valves)):
        d = min_distance(all_valves[i], all_valves[j], ())
        distances[(all_valves[i], all_valves[j])] = d
        distances[(all_valves[j], all_valves[i])] = d


def walk_graph(cur_valve, visited, valves, minutes_left, max_to_visit):
    # 'HH', 'JJ', 'DD', 'BB', 'EE', 'CC'
    # print(cur_valve, visited, valves, minutes_left)
    if (minutes_left <= 1) or (len(valves) == 0):
        return 0
    max_pressure_relieved = 0
    for i in range(len(valves)):
        # print("starting from", cur_valve, "with", len(valves), "valves left")
        valve = valves[i]
        if distances[(cur_valve, valve)] < (minutes_left - 1):
            minutes_left_this = minutes_left - (distances[(cur_valve, valve)] + 1)
            pressure_relieved = (minutes_left_this * flow_rates[valve])
            if (len(visited) + 1) == max_to_visit:
                pressure_relieved += walk_graph('AA', visited + [valve], valves[:i] + valves[i + 1:], 26, 100000)
            else:
                pressure_relieved += walk_graph(valve, visited + [valve], valves[:i] + valves[i + 1:], minutes_left_this, max_to_visit)
            if pressure_relieved > max_pressure_relieved:
                # print("Highest pressure relived:", pressure_relieved)
                max_pressure_relieved = pressure_relieved
    return max_pressure_relieved


all_valves = [v for v in all_valves if flow_rates[v] > 0]
max_p = 0
for max_to_visit in range(1, len(all_valves)):
    pressure = walk_graph('AA', [], all_valves, 26, max_to_visit)
    max_p = max(max_p, pressure)
    print(datetime.datetime.now(), max_p)
print(max_p)
