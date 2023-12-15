from collections import defaultdict


def hash_str(s):
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256
    return value


with open("input.txt") as file:
    steps = file.read().split(",")

boxes = defaultdict(list)

for step in steps:
    if "-" in step:
        label = step.split("-")[0]
        box_id = hash_str(label)
        for lens in boxes[box_id]:
            if label == lens[0]:
                boxes[box_id].remove(lens)
    else:
        label, focal_length = step.split("=")
        box_id = hash_str(label)
        focal_length = int(focal_length)
        is_replaced = False
        for lens in boxes[box_id]:
            if label == lens[0]:
                lens[1] = focal_length
                is_replaced = True
                break
        if not is_replaced:
            boxes[box_id].append([label, focal_length])

focusing_power = 0
for box_id, lenses in boxes.items():
    for slot_number, lens in zip(range(1, len(lenses) + 1), lenses):
        focusing_power += (box_id + 1) * slot_number * lens[1]

print(focusing_power)
