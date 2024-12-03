import re

with open("input.txt") as file:
    memory = file.read()

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
print(matches)

multiplications_sum = 0
for match in matches:
    a, b = match[4:-1].split(',')
    multiplications_sum += int(a) * int(b)

print(multiplications_sum)