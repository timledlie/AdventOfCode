with open("input.txt") as file:
    lines = file.readlines()

time = int(''.join(lines[0].strip().split(":")[1].split()))
distance = int(''.join(lines[1].strip().split(":")[1].split()))

answer = 0
for j in range(1, time // 2):
    if j * (time - j) > distance:
        if time % 2 == 0:
            answer = (time // 2 - j) * 2 + 1
            break
        else:
            answer = (time // 2 - j + 1) * 2
            break

print(answer)
