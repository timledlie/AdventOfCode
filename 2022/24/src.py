from collections import defaultdict

blizzard_locations = set()
ups, rights, downs, lefts = set(), set(), set(), set()
with open("input_sample.txt") as file:
    x, y = 0, 0
    n_rows, n_cols = 0, 0
    for line in file.readlines()[1:-1]:
        n_rows += 1
        n_cols = len(line) - 3
        for char in line[1:-2]:
            if char != '.':
                blizzard_locations.add((x, y))
            if char == '^':
                ups.add((x, y))
            elif char == '>':
                rights.add((x, y))
            elif char == 'v':
                downs.add((x, y))
            elif char == '<':
                lefts.add((x, y))
            x += 1
        x = 0
        y += 1


def step_blizzards(ups, rights, downs, lefts, n_rows, n_cols):
    blizzard_locations_next, ups_next, rights_next, downs_next, lefts_next = set(), set(), set(), set(), set()
    for up in ups:
        x, y = up
        if y == 0:
            new_point = (x, n_rows - 1)
            ups_next.add(new_point)
        else:
            new_point = (x, y - 1)
            ups_next.add(new_point)
        blizzard_locations_next.add(new_point)
    for right in rights:
        x, y = right
        if x == n_cols - 1:
            new_point = (0, y)
            rights_next.add(new_point)
        else:
            new_point = (x + 1, y)
            rights_next.add(new_point)
        blizzard_locations_next.add(new_point)
    for down in downs:
        x, y = down
        if y == n_rows - 1:
            new_point = (x, 0)
            downs_next.add(new_point)
        else:
            new_point = (x, y + 1)
            downs_next.add(new_point)
        blizzard_locations_next.add(new_point)
    for left in lefts:
        x, y = left
        if x == 0:
            new_point = (n_cols - 1, y)
            lefts_next.add(new_point)
        else:
            new_point = (x - 1, y)
            lefts_next.add(new_point)
        blizzard_locations_next.add(new_point)

    return blizzard_locations_next, ups_next, rights_next, downs_next, lefts_next


# print(blizzard_locations)
# for i in range(7):
#     blizzard_locations, ups, rights, downs, lefts = step_blizzards(ups, rights, downs, lefts, n_rows, n_cols)
#     print(blizzard_locations)

blizzard_locations, ups, rights, downs, lefts = step_blizzards(ups, rights, downs, lefts, n_rows, n_cols)
blizzard_locations, ups, rights, downs, lefts = step_blizzards(ups, rights, downs, lefts, n_rows, n_cols)
exit()

step = 0
start_position = (0, -1)
visited_permutations = defaultdict(set)
visited_permutations[start_position].add((tuple(ups), tuple(rights), tuple(downs), tuple(lefts)))
current_positions = {start_position}
while True:
    step += 1
    next_positions = set()
    blizzard_locations, ups, rights, downs, lefts = step_blizzards(ups, rights, downs, lefts, n_rows, n_cols)
    for pos in current_positions:
        # consider waiting
        if (tuple(ups), tuple(rights), tuple(downs), tuple(lefts)) not in visited_permutations[pos]:
            next_positions.add(pos)
            visited_permutations[pos].add((tuple(ups), tuple(rights), tuple(downs), tuple(lefts)))
        if pos == start_position:
            if (0, 0) not in blizzard_locations and (tuple(ups), tuple(rights), tuple(downs), tuple(lefts)) not in visited_permutations[(0, 0)]:
                next_positions.add((0, 0))
                visited_permutations[(0, 0)].add((tuple(ups), tuple(rights), tuple(downs), tuple(lefts)))
        else:
            if pos[1] > 0:
                pos_next = (pos[0], pos[1] - 1)
                if pos_next not in blizzard_locations and (tuple(ups), tuple(rights), tuple(downs), tuple(lefts)) not in visited_permutations[pos_next]:
                    next_positions.add(pos_next)
                    visited_permutations[pos_next].add((tuple(ups), tuple(rights), tuple(downs), tuple(lefts)))
            if pos[0] < n_cols - 2:
                pos_next = (pos[0] + 1, pos[1])
                if pos_next not in blizzard_locations and (tuple(ups), tuple(rights), tuple(downs), tuple(lefts)) not in visited_permutations[pos_next]:
                    next_positions.add(pos_next)
                    visited_permutations[pos_next].add((tuple(ups), tuple(rights), tuple(downs), tuple(lefts)))
            if pos[1] < n_rows - 2:
                pos_next = (pos[0], pos[1] + 1)
                if pos_next not in blizzard_locations and (tuple(ups), tuple(rights), tuple(downs), tuple(lefts)) not in visited_permutations[pos_next]:
                    next_positions.add(pos_next)
                    visited_permutations[pos_next].add((tuple(ups), tuple(rights), tuple(downs), tuple(lefts)))
            if pos[0] > 0:
                pos_next = (pos[0] - 1, pos[1])
                if pos_next not in blizzard_locations and (tuple(ups), tuple(rights), tuple(downs), tuple(lefts)) not in visited_permutations[pos_next]:
                    next_positions.add(pos_next)
                    visited_permutations[pos_next].add((tuple(ups), tuple(rights), tuple(downs), tuple(lefts)))
    current_positions = next_positions
    if (n_cols - 1, n_rows - 1) in current_positions:
        break

print(step + 1)