with (open("input.txt") as f):
    input_text = f.read()

fresh_ranges_text, available_ingredients_text = input_text.split("\n\n")

fresh_ranges = [tuple(map(int, line.split('-'))) for line in fresh_ranges_text.splitlines()]
available_ingredients = tuple(map(int, available_ingredients_text.splitlines()))

n_fresh_ingredients = 0
for ingredient in available_ingredients:
    for fresh_range in fresh_ranges:
        if fresh_range[0] <= ingredient <= fresh_range[1]:
            n_fresh_ingredients += 1
            break

print(n_fresh_ingredients)
