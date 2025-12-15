import functools

with (open("input_sample.txt") as f):
    grid = [line.strip() for line in f.readlines()]

@functools.cache
def count_timelines(row, beam_col):
    if row == len(grid):
        return 1

    if grid[row][beam_col] == '^':
        return count_timelines(row + 1, beam_col - 1) + count_timelines(row + 1, beam_col + 1)
    else:
        return count_timelines(row + 1, beam_col)

print(count_timelines(2, grid[0].index('S')))
