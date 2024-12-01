from collections import defaultdict

left_list, right_list = [], []
right_list_counts = defaultdict(int)
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
        right_list_counts[int(right)] += 1

similarity_score = 0
for n in left_list:
    similarity_score += n * right_list_counts[n]

print(similarity_score)