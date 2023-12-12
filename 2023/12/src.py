def count_valid_arrangements(chars, groupings):
    if len(groupings) == 0:
        if len(chars) == (chars.count(".") + chars.count("?")):
            return 1
        else:
            return 0

    if len(chars) == 0:
        return 0

    if chars[0] == ".":
        return count_valid_arrangements(chars[1:], groupings)

    if chars[0] == "#":
        if len(chars) >= groupings[0] and (groupings[0] * "#") == chars[:groupings[0]].replace("?", "#"):
            if len(chars) == groupings[0]:
                return count_valid_arrangements(chars[groupings[0]:], groupings[1:])
            if chars[groupings[0]] in (".", "?"):
                return count_valid_arrangements(chars[groupings[0] + 1:], groupings[1:])
        return 0

    if chars[0] == "?":
        return count_valid_arrangements("." + chars[1:], groupings) + \
               count_valid_arrangements("#" + chars[1:], groupings)


total_valid_mappings = 0
with open("input.txt") as file:
    for line in file.readlines():
        chars, groupings = line.strip().split()
        groupings = [int(n) for n in groupings.split(",")]
        total_valid_mappings += count_valid_arrangements(chars, groupings)

print(total_valid_mappings)
