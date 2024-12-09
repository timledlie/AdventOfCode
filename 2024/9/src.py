with open("input.txt") as file:
    disk_map = [int(char) for char in file.read()]

blocks = []

for i in range(len(disk_map)):
    if i % 2 == 0:
        blocks += [i // 2] * disk_map[i]
    else:
        blocks += ["."] * disk_map[i]

left_index = None
for i in range(len(blocks)):
    if blocks[i] == ".":
        left_index = i
        break

right_index = None
for i in range(len(blocks) - 1, -1, -1):
    if blocks[i] != ".":
        right_index = i
        break

while left_index < right_index:
    blocks[left_index] = blocks[right_index]
    blocks[right_index] = "."

    left_index += 1
    right_index -= 1

    while (blocks[left_index] != ".") and (left_index <= right_index):
        left_index += 1

    while (blocks[right_index] == ".") and (left_index <= right_index):
        right_index -= 1

checksum = 0
for i in range(len(blocks)):
    if blocks[i] == ".":
        break
    checksum += i * blocks[i]

print(checksum)
