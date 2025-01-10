cache = {}
def count_design_options(design, patterns):
    if len(design) == 0:
        return 1

    if design in cache:
        return cache[design]

    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += count_design_options(design[len(pattern):], patterns)

    cache[design] = count
    return count


with open("input.txt") as file:
    text_input = file.read()

patterns_text, designs_text = text_input.strip().split("\n\n")
patterns = patterns_text.strip().split(", ")
designs = designs_text.strip().split("\n")

print(sum([count_design_options(design, patterns) for design in designs]))
