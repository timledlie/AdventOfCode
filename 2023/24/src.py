import itertools


def point_of_intersection(line1, line2):
    ((x1, y1), (x2, y2)), ((x3, y3), (x4, y4)) = line1, line2

    line1_infinite_slope = (x2 - x1) == 0
    line2_infinite_slope = (x4 - x3) == 0
    if line1_infinite_slope and line2_infinite_slope:
        return None, None

    if not line1_infinite_slope and not line2_infinite_slope:
        line1_slope = (y2 - y1) / (x2 - x1)
        line2_slope = (y4 - y3) / (x4 - x3)
        if abs(line1_slope - line2_slope) < .0000000001:
            return None, None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / \
         ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / \
         ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    return px, py


def is_same_sign_or_both_zero(i1, i2):
    if (i1 == i2) and (i1 == 0):
        return True
    if (i1 == 0) or (i2 == 0):
        return False
    return (abs(i1) // i1) == (abs(i2) // i2)


lines = []
with open("input.txt") as file:
    for line in file.readlines():
        position_text, velocity_text = line.strip().split("@")
        x, y, z = [int(c) for c in position_text.split(", ")]
        dx, dy, dz = [int(c) for c in velocity_text.split(", ")]
        lines.append(((x, y), (x + dx, y + dy)))

test_area_min, test_area_max = 200000000000000, 400000000000000
n_intersections_within_test_area = 0
for line1, line2 in itertools.combinations(lines, 2):
    px, py = point_of_intersection(line1, line2)
    if px is not None:
        if (test_area_min <= px <= test_area_max) and (test_area_min <= py <= test_area_max):
            ((x1, y1), (x2, y2)), ((x3, y3), (x4, y4)) = line1, line2
            if is_same_sign_or_both_zero(px - x2, x2 - x1) and is_same_sign_or_both_zero(py - y2, y2 - y1) and \
               is_same_sign_or_both_zero(px - x4, x4 - x3) and is_same_sign_or_both_zero(py - y4, y4 - y3):
                n_intersections_within_test_area += 1

print(n_intersections_within_test_area)
