# n_fallen = 12
# dim = 7
n_fallen = 1024
dim = 71
with open("input.txt") as file:
    byte_positions = [(int(a), int(b)) for a, b in [line.strip().split(",") for line in file.readlines()]]


def is_path(n_corrupted):
    corrupted_positions = byte_positions[:n_corrupted]
    frontier = [(0, 0)]
    visited = {(0, 0)}
    exit_position = (dim - 1, dim - 1)
    while len(frontier) > 0:
        frontier_next = []
        for x, y in frontier:
            if (x, y) == exit_position:
                return True
            for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (0 <= x + dx < dim) and (0 <= y + dy < dim):
                    candidate = (x + dx, y + dy)
                    if (candidate not in visited) and (candidate not in corrupted_positions):
                        frontier_next.append(candidate)
                        visited.add(candidate)
        frontier = frontier_next
    return False


low, high = 0, len(byte_positions)
while (high - low) > 1:
    mid = (low + high) // 2
    if is_path(mid):
        low = mid
    else:
        high = mid

print(byte_positions[(low + high) // 2])
