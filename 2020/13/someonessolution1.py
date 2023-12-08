import sys

a, b = open("input.txt").read().strip().split("\n")
timestamp = int(a)
busses = [(i, int(x)) for i, x in enumerate(b.split(",")) if x != "x"]

# Part 1.
min_wait = sys.maxsize
part1 = None

# Part 2.
d = 1
i = 0

for offset, bus in busses:
    # Part 1. 
    loops = -(timestamp // -bus)
    wait = loops * bus - timestamp
    if wait < min_wait:
        part1 = wait * bus
        min_wait = wait

    # Part 2.
    while True:
        i += d
        if (i + offset) % bus == 0:
            d = d * bus
            break

print(part1)
print(i)