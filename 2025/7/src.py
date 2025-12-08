with (open("input.txt") as f):
    grid = [line.strip() for line in f.readlines()]

count_splits = 0
incoming_beams = {grid[0].index('S')}
for row in range(2, len(grid) - 1):
    incoming_beams_next = set()
    for i in incoming_beams:
        if grid[row][i] == '^':
            count_splits += 1
            incoming_beams_next.update((i - 1, i + 1))
        else:
            incoming_beams_next.add(i)
    incoming_beams = incoming_beams_next

print(count_splits)
