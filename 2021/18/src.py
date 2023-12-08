# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
import math
import json

snailfish_numbers = []
with open("input.txt") as file:
    for line in file.readlines():
        snailfish_numbers.append(line.strip())


def add(s1, s2):
    return "[" + s1 + "," + s2 + "]"


def reduce_explode(s):
    skip_indexes = []
    s_reduced = ""
    previous_num = previous_num_index = add_to_next_num = None
    depth = 0
    for i in range(len(s)):
        if i in skip_indexes:
            continue
        c = s[i]
        if c == "[":
            depth += 1
            s_reduced += c
        elif c == "]":
            depth -= 1
            s_reduced += c
        elif c == ",":
            s_reduced += c
        elif c.isdigit():
            if s[i+1].isdigit():
                n = int(s[i:i+2])
                is_two_digit = True
            else:
                n = int(s[i])
                is_two_digit = False
            if add_to_next_num is not None:
                if is_two_digit:
                    s_reduced += str(n + add_to_next_num) + s[i + 2:]
                else:
                    s_reduced += str(n + add_to_next_num) + s[i + 1:]
                break
            elif depth > 4:
                if previous_num is not None:
                    new_num = str(previous_num + n)
                    if previous_num > 9:
                        s_reduced = s_reduced[:previous_num_index] + new_num + s_reduced[previous_num_index+2:]
                    else:
                        s_reduced = s_reduced[:previous_num_index] + new_num + s_reduced[previous_num_index+1:]
                if is_two_digit:
                    if s[i+4].isdigit():
                        add_to_next_num = int(s[i + 3:i + 5])
                        skip_indexes += [i+1, i+2, i+3, i+4, i+5]
                    else:
                        add_to_next_num = int(s[i + 3:i + 4])
                        skip_indexes += [i+1, i+2, i+3, i+4]
                else:
                    if s[i+3].isdigit():
                        add_to_next_num = int(s[i + 2:i + 4])
                        skip_indexes += [i+1, i+2, i+3, i+4]
                    else:
                        add_to_next_num = int(s[i + 2:i + 3])
                        skip_indexes += [i+1, i+2, i+3]
                depth -= 1
                s_reduced = s_reduced[:-1] + '0'
                continue
            else:
                previous_num = n
                previous_num_index = i
                if previous_num > 9:
                    skip_indexes += [i+1]
                s_reduced += str(n)
    return s_reduced


def reduce_split(s):
    s_reduced = ""
    for i in range(len(s)):
        c = s[i]
        if c == "[":
            s_reduced += c
        elif c == "]":
            s_reduced += c
        elif c == ",":
            s_reduced += c
        elif c.isdigit() and s[i+1].isdigit():
                n = int(s[i:i+2])
                n1 = math.floor(float(n) / 2.0)
                n2 = math.ceil(float(n) / 2.0)
                s_reduced += "[" + str(n1) + "," + str(n2) + "]" + s[i + 2:]
                break
        else:
            s_reduced += str(c)
    return s_reduced


def reduce(s):
    while True:
        s_reduced = reduce_explode(s)
        changes_made = s != s_reduced
        if changes_made:
            s = s_reduced
            continue

        s_reduced = reduce_split(s)
        changes_made = s != s_reduced
        if changes_made:
            s = s_reduced
            continue

        break
    return s


def magnitude(s):
    return magnitude_recursive(json.loads(s))


def magnitude_recursive(l):
    left = l[0]
    right = l[1]
    if isinstance(left, list):
        left = magnitude_recursive(left)
    if isinstance(right, list):
        right = magnitude_recursive(right)
    return 3 * left + 2 * right


def test():
    cases = {
        "[[[[[9,8],1],2],3],4]": "[[[[0,9],2],3],4]",
        "[7,[6,[5,[4,[3,2]]]]]": "[7,[6,[5,[7,0]]]]",
        "[[6,[5,[4,[3,2]]]],1]": "[[6,[5,[7,0]]],3]",
        "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]": "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
    }
    for input, output in cases.items():
        print(input)
        if output != reduce(input):
            print("FAIL:", output, reduce((input)))

def test_magnitude():
    cases = {
        "[9,1]": 29,
        "[1,9]": 21,
        "[[9,1],[1,9]]": 129,
        "[[1,2],[[3,4],5]]": 143,
        "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]": 1384,
        "[[[[1,1],[2,2]],[3,3]],[4,4]]": 445,
        "[[[[3,0],[5,3]],[4,4]],[5,5]]": 791,
        "[[[[5,0],[7,4]],[5,5]],[6,6]]": 1137,
        "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]": 3488
    }
    for input, output in cases.items():
        print(input)
        if output != magnitude(input):
            print("FAIL:", output, magnitude((input)))


# s = "[[14,[[[3,7],[4,3]],[[6,3],[8,8]]]]]"
# print(reduce(s))

# test()
# test_magnitude()

# running_sum = snailfish_numbers.pop(0)
# while len(snailfish_numbers):
#     sn = snailfish_numbers.pop(0)
#     running_sum = reduce(add(running_sum, sn))
# print(running_sum)
# print(magnitude(running_sum))

largest = 0
for i in range(len(snailfish_numbers) - 1):
    for j in range(i + 1, len(snailfish_numbers)):
        mag1 = magnitude(reduce(add(snailfish_numbers[i], snailfish_numbers[j])))
        mag2 = magnitude(reduce(add(snailfish_numbers[j], snailfish_numbers[i])))
        largest = max(largest, mag1, mag2)
print(largest)