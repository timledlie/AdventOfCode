x = 1
cycle = 1
addx_value = None
is_during_addx = False
signal_strength_total = 0
next_signal_strength_reading = 20
drawing_position = 0
with open("input.txt") as file:
    while True:
        # print(cycle, x, cycle * x)
        if (x - 1) <= drawing_position <= (x + 1):
            print('#', end='')
        else:
            print('.', end='')
        if drawing_position // 39 == 1:
            drawing_position = 0
            print()
        else:
            drawing_position += 1

        # if cycle == next_signal_strength_reading:
        #     next_signal_strength_reading += 40
        #     signal_strength_total += cycle * x
        #     if next_signal_strength_reading > 220:
        #         break

        if not is_during_addx:
            line = file.readline().strip()
            if not line:
                break
            if line != "noop":
                is_during_addx = True
                addx_value = int(line.split()[1])
        else:
            is_during_addx = False
            x += addx_value
        cycle += 1

print(x)
print(signal_strength_total)
