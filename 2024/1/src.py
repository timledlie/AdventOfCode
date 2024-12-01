left_list, right_list = [], []
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

left_list.sort()
right_list.sort()

sum_distance = 0
for i in range(len(left_list)):
    sum_distance += abs(left_list[i] - right_list[i])

print(sum_distance)