with open("input.txt") as file:
    initial_secret_numbers = [int(line.strip()) for line in file.readlines()]

rounds = 2000
running_sum = 0
for n in initial_secret_numbers:
    for r in range(rounds):
        m = n * 64
        n = m ^ n
        n = n % 16777216

        m = n // 32
        n = m ^ n
        n = n % 16777216

        m = n * 2048
        n = m ^ n
        n = n % 16777216
    running_sum += n
print(running_sum)
