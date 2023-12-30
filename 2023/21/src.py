garden_coords, possible_coords = set(), set()
with open("input.txt") as file:
    lines = file.readlines()
    for y in range(len(lines)):
        line = lines[y].strip()
        for x in range(len(line)):
            if line[x] == ".":
                garden_coords.add((x, y))
            elif line[x] == "S":
                possible_coords = {(x, y)}
                garden_coords.add((x, y))

for step in range(64):
    possible_coords_next = set()
    for x, y in possible_coords:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (x + dx, y + dy) in garden_coords:
                possible_coords_next.add((x + dx, y + dy))
    possible_coords = possible_coords_next

print(len(possible_coords))
