def convert_to_sets(pattern_as_tuples):
    pattern_as_sets = []
    for pattern_tuple in pattern_as_tuples:
        rock_indexes = set()
        for i in range(len(pattern_tuple)):
            if pattern_tuple[i] == "#":
                rock_indexes.add(i)
        pattern_as_sets.append(rock_indexes)
    return pattern_as_sets


def find_reflection_index(pattern, n_off_by):
    for index in range(len(pattern) - 1):
        running_off_by = 0
        for a, b in zip(range(index, -1, -1), range(index + 1, len(pattern))):
            running_off_by += len(pattern[a] ^ pattern[b])
            if running_off_by > n_off_by:
                break
        if running_off_by == n_off_by:
            return index + 1  # the problem statement indexes starting at 1
    return 0


total = 0
n_off_by = 1
with open("input.txt") as file:
    for pattern_text in file.read().split("\n\n"):
        pattern_orig = [tuple(char) for char in pattern_text.strip().split()]
        pattern_rotated = [*zip(*pattern_orig)]  # reflect rows into columns
        pattern_orig = convert_to_sets(pattern_orig)
        pattern_rotated = convert_to_sets(pattern_rotated)
        total += 100 * find_reflection_index(pattern_orig, n_off_by) + find_reflection_index(pattern_rotated, n_off_by)

print(total)
