from operator import itemgetter

with (open("input.txt") as f):
    input_text = f.read()

fresh_ranges_text, *ignore = input_text.split("\n\n")

fresh_ranges = [tuple(map(int, line.split('-'))) for line in fresh_ranges_text.splitlines()]

fresh_ranges.sort(key=itemgetter(0))
fresh_ranges_merged = []
cur = fresh_ranges[0]
for i_next in range(1, len(fresh_ranges)):
    start1, end1 = cur
    start2, end2 = fresh_ranges[i_next]
    if start1 <= start2 <= end1:
        cur = (start1, max(end1, end2))
    else:
        fresh_ranges_merged.append(cur)
        cur = fresh_ranges[i_next]
fresh_ranges_merged.append(cur)

n_ingredients = 0
for fresh_range in fresh_ranges_merged:
    n_ingredients += fresh_range[1] - fresh_range[0] + 1

print(n_ingredients)
