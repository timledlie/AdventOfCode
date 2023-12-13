memo = {}


def count_valid_arrangements(chars, groupings):
    ret = None
    if (chars, groupings) in memo:
        return memo[(chars, groupings)]

    if len(groupings) == 0:
        if len(chars) == (chars.count(".") + chars.count("?")):
            ret = 1
        else:
            ret = 0

    elif len(chars) == 0:
        ret = 0

    elif chars[0] == ".":
        ret = count_valid_arrangements(chars[1:], groupings)

    elif chars[0] == "#":
        if len(chars) >= groupings[0] and (groupings[0] * "#") == chars[:groupings[0]].replace("?", "#"):
            if len(chars) == groupings[0]:
                ret = count_valid_arrangements(chars[groupings[0]:], groupings[1:])
            elif chars[groupings[0]] in (".", "?"):
                ret = count_valid_arrangements(chars[groupings[0] + 1:], groupings[1:])
            else:
                ret = 0
        else:
            ret = 0

    elif chars[0] == "?":
        ret = count_valid_arrangements("." + chars[1:], groupings) + \
              count_valid_arrangements("#" + chars[1:], groupings)

    memo[(chars, groupings)] = ret
    return ret


total_valid_mappings = 0
with open("input.txt") as file:
    for line in file.readlines():
        chars, groupings = line.strip().split()
        groupings = tuple([int(n) for n in groupings.split(",")])

        chars = "?".join([chars] * 5)
        groupings *= 5

        total_valid_mappings += count_valid_arrangements(chars, groupings)

print(total_valid_mappings)
