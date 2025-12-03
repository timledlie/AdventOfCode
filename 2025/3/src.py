with (open("input.txt") as f):
    banks = [tuple(map(int, bank.strip())) for bank in f.readlines()]

sum_joltages = 0
n_digits = 12
for bank in banks:
    max_digits = []
    lowest_possible_index, lowest_possible_index_next = 0, 0
    for n_left in range(n_digits, 0, -1):
        max_digit = 0
        for i in range(len(bank) - n_left, lowest_possible_index - 1, -1):
            if bank[i] >= max_digit:
                max_digit = bank[i]
                lowest_possible_index_next = i + 1
        max_digits.append(max_digit)
        lowest_possible_index = lowest_possible_index_next
    sum_joltages += int("".join(map(str, max_digits)))

print(sum_joltages)
