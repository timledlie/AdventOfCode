# using the Shoelace Formula: https://en.wikipedia.org/wiki/Shoelace_formula
area = 0
with open("input.txt") as file:
    x1, y1 = 0, 0
    for line in file.readlines():
        x2, y2 = x1, y1
        text = line.strip().split()[-1]
        distance, direction = int(text[2:7], 16), int(text[7:8])
        if direction == 0:
            x2 = x1 + distance
        elif direction == 1:
            y2 = y1 + distance
        elif direction == 2:
            x2 = x1 - distance
        elif direction == 3:
            y2 = y1 - distance
        area += (y1 + y2) * (x1 - x2) + distance # add distance to account for the 1-unit width of the trench
        x1, y1 = x2, y2

print(round(.5 * area) + 1)
