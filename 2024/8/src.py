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
        for step in (-1, 1):
            multiplier = 0
            while True:
                x, y = loc_a[0] + (multiplier * dx), loc_a[1] + (multiplier * dy)
                if (x < 0) or (x > max_x) or (y < 0) or (y > max_y):
                    break
                antinode_locations.add((x, y))
                multiplier += step

print(len(antinode_locations))
