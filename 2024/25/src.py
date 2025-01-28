from collections import defaultdict

with open("input.txt") as file:
    text_data = file.read()

dim = 5
locks, keys = [], []
for locks_keys_blocks in text_data.split("\n\n"):
    rows = locks_keys_blocks.split("\n")
    if rows[0] == "#####":
        lock = defaultdict(int)
        for row in range(1, dim + 1):
            for col in range(dim):
                if rows[row][col] == "#":
                    lock[col] += 1
        locks.append(lock)
    else:
        key = defaultdict(int)
        for row in range(dim, 0, -1):
            for col in range(dim):
                if rows[row][col] == "#":
                    key[col] += 1
        keys.append(key)


def does_key_fit_in_lock(key, lock):
    for col in range(dim):
        if key[col] + lock[col] > dim:
            return False
    return True


n_fit = 0
for key in keys:
    for lock in locks:
        if does_key_fit_in_lock(key, lock):
            n_fit += 1
print(n_fit)
