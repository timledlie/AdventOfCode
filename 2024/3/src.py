import re

with open("input.txt") as file:
    memory = file.read()

multiplications_sum = 0
on_segments = memory.split("do()")
for on_segment in on_segments:
    on_subsegment = on_segment.split("don't()")[0]
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", on_subsegment)
    for match in matches:
        a, b = match[4:-1].split(',')
        multiplications_sum += int(a) * int(b)

print(multiplications_sum)