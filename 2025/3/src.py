with (open("input.txt") as f):
    banks = [tuple(map(int, bank.strip())) for bank in f.readlines()]

sum_joltage = 0
for bank in banks:
    a, b = bank[0], bank[1]
    for i in range(1, len(bank) - 1):
        if bank[i] > a:
            a = bank[i]
            b = bank[i + 1]
        elif bank[i] > b:
            b = bank[i]
    if bank[-1] > b:
        b = bank[-1]
    sum_joltage += a * 10 + b

print(sum_joltage)
