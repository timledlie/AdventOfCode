topo_map = []
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        topo_map.append([-1] + [int(char) for char in line] + [-1])

topo_map = [[-1] * len(topo_map[0])] + topo_map + [[-1] * len(topo_map[0])]
n_rows, n_cols = len(topo_map), len(topo_map[0])

trailheads = []
for row in range(n_rows):
    for col in range(n_cols):
        if topo_map[row][col] == 0:
            trailheads.append((row, col))


def get_trailhead_score(trailhead, topo_map):
    cur_locations = [trailhead]
    cur_height = 0
    while True:
        next_locations = set()
        for row, col in cur_locations:
            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if topo_map[row + delta_row][col + delta_col] == (cur_height + 1):
                    next_locations.add((row + delta_row, col + delta_col))

        if cur_height == 8:
            return len(next_locations)
        if len(next_locations) == 0:
            return 0

        cur_locations = next_locations
        cur_height += 1


total_scores = 0
for trailhead in trailheads:
    total_scores += get_trailhead_score(trailhead, topo_map)

print(total_scores)
