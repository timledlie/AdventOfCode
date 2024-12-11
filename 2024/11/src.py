with open("input.txt") as file:
    stones = [int(stone) for stone in file.read().strip().split()]

blinks = 25
for blink in range(blinks):
    next_stones = []
    for stone in stones:
        if stone == 0:
            next_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            next_stones.extend([int(str(stone)[:len(str(stone)) // 2]), int(str(stone)[len(str(stone)) // 2:])])
        else:
            next_stones.append(2024 * stone)
    stones = next_stones

print(len(stones))
