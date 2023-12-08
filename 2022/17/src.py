with open("input.txt") as file:
    jets = file.read().strip()


def generate_rock_points(rock_type, max_height):
    bottom = max_height + 4
    if rock_type == 0:
        return {(2, bottom), (3, bottom), (4, bottom), (5, bottom)}
    if rock_type == 1:
        return {(2, bottom + 1), (3, bottom), (3, bottom + 1), (3, bottom + 2), (4, bottom + 1)}
    if rock_type == 2:
        return {(2, bottom), (3, bottom), (4, bottom), (4, bottom + 1), (4, bottom + 2)}
    if rock_type == 3:
        return {(2, bottom), (2, bottom + 1), (2, bottom + 2), (2, bottom + 3)}
    if rock_type == 4:
        return {(2, bottom), (2, bottom + 1), (3, bottom), (3, bottom + 1)}
    return None


def apply_jet(jet, rock_points, all_rock_points):
    new_rock_points = set()
    change = 1 if jet == '>' else -1
    for point in rock_points:
        new_point = (point[0] + change, point[1])
        if (new_point[0] < 0) or (new_point[0] >= 7) or (new_point in all_rock_points):
            return rock_points
        new_rock_points.add(new_point)
    return new_rock_points


def apply_gravity(rock_points, all_rock_points):
    new_rock_points = set()
    for point in rock_points:
        new_point = (point[0], point[1] - 1)
        if (new_point[1] <= 0) or (new_point in all_rock_points):
            return rock_points
        new_rock_points.add(new_point)
    return new_rock_points


n_rocks = 2022
tower_height = 0
all_rock_points = set()
jet_index = 0
for rock_index in range(n_rocks):
    rock_type = rock_index % 5
    rock_points = generate_rock_points(rock_type, tower_height)
    while True:
        rock_points = apply_jet(jets[jet_index], rock_points, all_rock_points)
        jet_index = (jet_index + 1) % len(jets)

        rock_points_next = apply_gravity(rock_points, all_rock_points)
        if rock_points_next == rock_points:
            all_rock_points |= rock_points
            for point in rock_points:
                tower_height = max(tower_height, point[1])
            break
        else:
            rock_points = rock_points_next

print(tower_height)