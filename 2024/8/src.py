import itertools

frequencies = []
antenna_locations = {}
antinode_locations = set()
y = 0
with open("input.txt") as file:
    for line in file.readlines():
        x = 0
        line = line.strip()
        for char in line:
            if char != ".":
                if char not in frequencies:
                    frequencies.append(char)
                    antenna_locations[char] = [(x, y)]
                else:
                    antenna_locations[char].append((x, y))
            x += 1
        y += 1
max_x, max_y = x - 1, y - 1

for frequency in frequencies:
    for loc_a, loc_b in itertools.combinations(antenna_locations[frequency], 2):
        dx, dy = loc_a[0] - loc_b[0], loc_a[1] - loc_b[1]
        x, y = loc_a[0] + dx, loc_a[1] + dy
        if (0 <= x <= max_x) and (0 <= y <= max_y):
            antinode_locations.add((x, y))

        x, y = loc_b[0] - dx, loc_b[1] - dy
        if (0 <= x <= max_x) and (0 <= y <= max_y):
            antinode_locations.add((x, y))

print(len(antinode_locations))
