with open("input.txt") as file:
    disk_map = [int(char) for char in file.read()]

blocks = []
file_info = {}
file_id = None
for i in range(len(disk_map)):
    if i % 2 == 0:
        file_id = i // 2
        block_start = len(blocks)
        blocks += [file_id] * disk_map[i]
        file_info[file_id] = {"start": block_start, "length": disk_map[i]}
    else:
        blocks += ["."] * disk_map[i]
max_file_id = file_id


def find_free_space(blocks, length, rightmost_index):
    index = 0
    start, end = None, None
    while index < rightmost_index:
        if blocks[index] == ".":
            if start is None:
                start = index
            end = index + 1
            if end - start == length:
                return start
        else:
            start, end = None, None
        index += 1
    return None


for file_id in range(max_file_id, 0, -1):
    index = find_free_space(blocks, file_info[file_id]["length"], file_info[file_id]["start"])
    if index is not None:
        for offset in range(file_info[file_id]["length"]):
            blocks[index + offset] = file_id
            blocks[file_info[file_id]["start"] + offset] = "."

checksum = 0
for i in range(len(blocks)):
    if blocks[i] != ".":
        checksum += i * blocks[i]

print(checksum)
