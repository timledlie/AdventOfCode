with open("input.txt") as f:
    rotations = f.readlines()

dial = 50
n_zeros = 0
for rotation in rotations:
    direction, amount = rotation[0], int(rotation[1:])
    is_dial_starts_at_zero = dial == 0

    # first count number of complete rotations
    n_zeros += amount // 100

    # next move the dial the incremental amount
    if direction == "L":
        dial -= amount % 100
    else:
        dial += amount % 100

    # if we have hit zero during the incremental movement, count one more
    if not is_dial_starts_at_zero and ((dial <= 0) or (dial >= 100)):
        n_zeros += 1

    # normalize to our 0 - 99 range
    dial %= 100

print(n_zeros)
