from collections import defaultdict


with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

row_max, col_max = len(lines), len(lines[0])
star_coords = set()
for row in range(row_max):
    for col in range(col_max):
        char = lines[row][col]
        if char == '*':
            star_coords.add((row, col))

numbers = []
for row in range(row_max):
    number = ''
    col_start, col_end = 0, 0
    is_capturing_number = False
    for col in range(col_max):
        char = lines[row][col]
        if is_capturing_number:
            if char.isnumeric():
                number += char
                col_end = col
            else:
                numbers.append((row, (col_start, col_end), int(number)))
                number = ''
                col_start, col_end = 0, 0
                is_capturing_number = False
        else:
            if char.isnumeric():
                is_capturing_number = True
                col_start, col_end = col, col
                number = char
    if is_capturing_number:
        numbers.append((row, (col_start, col_end), int(number)))

star_adjacents = defaultdict(list)
for row, col_span, number in numbers:
    if (row, col_span[0] - 1) in star_coords:
        star_adjacents[(row, col_span[0] - 1)].append(number)
    if (row, col_span[1] + 1) in star_coords:
        star_adjacents[(row, col_span[1] + 1)].append(number)
    for col in range(col_span[0] - 1, col_span[1] + 2):
        if (row - 1, col) in star_coords:
            star_adjacents[(row - 1, col)].append(number)
        if (row + 1, col) in star_coords:
            star_adjacents[(row + 1, col)].append(number)

gear_ratios_sum = 0
for numbers in star_adjacents.values():
    if len(numbers) == 2:
        gear_ratios_sum += numbers[0] * numbers[1]

print(gear_ratios_sum)
