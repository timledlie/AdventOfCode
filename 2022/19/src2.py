quality = 0
with open("input2.txt") as file:
    for line in file.readlines():
        index, geodes = line.strip().split(' ')
        index, geodes = int(index), int(geodes)
        quality += index * geodes
print(quality)