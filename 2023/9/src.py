def predict_previous_value(history):
    if len(set(history)) == 1:
        return history[0]

    history_difference = []
    for i in range(len(history) - 1):
        history_difference.append(history[i + 1] - history[i])
    return history[0] - predict_previous_value(history_difference)


sum_previous_values = 0
with open("input.txt") as file:
    for line in file.readlines():
        history = [int(c) for c in line.strip().split()]
        sum_previous_values += predict_previous_value(history)

print(sum_previous_values)
