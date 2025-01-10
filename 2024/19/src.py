def is_design_possible(design, patterns):
    if len(design) == 0:
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if is_design_possible(design[len(pattern):], patterns):
                return True

    return False


with open("input.txt") as file:
    text_input = file.read()

patterns_text, designs_text = text_input.strip().split("\n\n")
patterns = patterns_text.strip().split(", ")
designs = designs_text.strip().split("\n")

print(sum([is_design_possible(design, patterns) for design in designs]))
