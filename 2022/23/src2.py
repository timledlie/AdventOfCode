def get_elf_bounds(elves):
    min_row, max_row, min_col, max_col = 10000000, 0, 10000000, 0
    for elf in elves:
        min_row = min(min_row, elf[0])
        max_row = max(max_row, elf[0])
        min_col = min(min_col, elf[1])
        max_col = max(max_col, elf[1])
    return min_row, max_row, min_col, max_col


def print_elves(elves):
    min_row, max_row, min_col, max_col = get_elf_bounds(elves)
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print("\n")


def count_empty_tiles_in_smallest_region(elves):
    min_row, max_row, min_col, max_col = get_elf_bounds(elves)
    return ((max_row - min_row + 1) * (max_col - min_col + 1)) - len(elves)


def get_new_position(elf, elves, orientation):
    nw = (elf[0] - 1, elf[1] - 1)
    nn = (elf[0] - 1, elf[1])
    ne = (elf[0] - 1, elf[1] + 1)
    ee = (elf[0], elf[1] + 1)
    se = (elf[0] + 1, elf[1] + 1)
    ss = (elf[0] + 1, elf[1])
    sw = (elf[0] + 1, elf[1] - 1)
    ww = (elf[0], elf[1] - 1)
    if {nw, nn, ne, ee, se, ss, sw, ww} & elves == set():
        return elf

    orientation_map = {
        0: {nw, nn, ne},  # north
        1: {sw, ss, se},  # south
        2: {nw, ww, sw},  # west
        3: {ne, ee, se},  # east
    }

    for i in range(4):
        if orientation == 0 and orientation_map[0] & elves == set():
            return nn
        if orientation == 1 and orientation_map[1] & elves == set():
            return ss
        if orientation == 2 and orientation_map[2] & elves == set():
            return ww
        if orientation == 3 and orientation_map[3] & elves == set():
            return ee
        orientation = (orientation + 1) % 4
    return elf


elves = set()
with open("input.txt") as file:
    row = 0
    while True:
        line = file.readline().strip()
        if not line:
            break
        for col in range(len(line)):
            if line[col] == '#':
                elves.add((row, col))
        row += 1

# print_elves(elves)

orientation = 0
count = 0
for i in range(1000):
    print(i)
    proposed_positions = {}
    new_elves = set()
    for elf in elves:
        proposed_positions[elf] = get_new_position(elf, elves, orientation)
    all_proposed_positions = list(proposed_positions.values())
    for elf, proposed_position in proposed_positions.items():
        if all_proposed_positions.count(proposed_position) > 1:
            new_elves.add(elf)
        else:
            new_elves.add(proposed_position)
    if new_elves == elves:
        print("SAME", i + 1)
        break
    elves = new_elves
    orientation = (orientation + 1) % 4
    # print("End of round", i + 1)
    # print_elves(elves)

# print(count_empty_tiles_in_smallest_region(elves))