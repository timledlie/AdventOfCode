with (open("input.txt") as f):
    lines = f.readlines()

numbers = [line[:-1] for line in lines[:-1]]
operations = lines[-1]

column_widths = []
column_start_indexes = [0]
width = 0
for i in range(1, len(operations)):
    if operations[i] == ' ':
        width += 1
    else:
        column_widths.append(width)
        column_start_indexes.append(i)
        width = 0
column_widths.append(width + 1)

grand_total = 0
operation_index = 0
for col in range(len(column_start_indexes)):
    start_index = column_start_indexes[col]
    width = column_widths[col]
    operation = operations[start_index]

    column_numbers = []
    for w in range(width):
        column_numbers.append(''.join([numbers[row][start_index + w] for row in range(len(numbers))]))
    grand_total += eval(operation.join(column_numbers))

print(grand_total)
