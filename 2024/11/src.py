from collections import defaultdict

stone_counts = defaultdict(int)
with open("input.txt") as file:
    for stone in file.read().strip().split():
        stone_counts[int(stone)] = 1

blinks = 75
for blink in range(blinks):
    next_stone_counts = defaultdict(int)
    for stone in stone_counts.keys():
        if stone == 0:
            next_stone_counts[1] += stone_counts[stone]
        elif len(str(stone)) % 2 == 0:
            next_stone_counts[int(str(stone)[:len(str(stone)) // 2])] += stone_counts[stone]
            next_stone_counts[int(str(stone)[len(str(stone)) // 2:])] += stone_counts[stone]
        else:
            next_stone_counts[2024 * stone] += stone_counts[stone]
    stone_counts = next_stone_counts

total_stones = 0
for stone in stone_counts.keys():
    total_stones += stone_counts[stone]

print(total_stones)
