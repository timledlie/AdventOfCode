with open("input.txt") as file:
    steps = file.read().split(",")

results_sum = 0
for step in steps:
    value = 0
    for char in step:
        value += ord(char)
        value *= 17
        value %= 256
    results_sum += value

print(results_sum)
