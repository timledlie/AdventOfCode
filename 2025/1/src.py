with open("input.txt") as f:
    rotations = f.readlines()

dial = 50
n_zeros = 0
for rotation in rotations:
    direction, amount = rotation[0], int(rotation[1:])
    if direction == "L":
        dial -= amount
    else:
        dial += amount
    dial %= 100
    if dial == 0:
        n_zeros += 1

print(n_zeros)
