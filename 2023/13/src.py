def rotate_clockwise_90(pattern):
    rotated_rows = [[] for _ in range(len(pattern[0]))]
    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            rotated_rows[col].append(pattern[row][col])
    return rotated_rows


def find_reflection_index(pattern):
    for index in range(len(pattern) - 1):
        is_reflection_point = True
        for a, b in zip(range(index, -1, -1), range(index + 1, len(pattern))):
            if pattern[a] != pattern[b]:
                is_reflection_point = False
        if is_reflection_point:
            return index + 1  # the problem statement indexes starting at 1
    return 0


patterns = []
total = 0
with open("input.txt") as file:
    for pattern_text in file.read().split("\n\n"):
        pattern = [list(row) for row in pattern_text.strip().split()]
        total += 100 * find_reflection_index(pattern) + find_reflection_index(rotate_clockwise_90(pattern))

print(total)
