from itertools import repeat

with open("input.txt") as file:
    signal = [int(el) for el in list(file.readline().strip())]


def make_pattern(n):
    return tuple(repeat(0, n - 1)) + tuple(repeat(1, n)) + tuple(repeat(0, n)) + tuple(repeat(-1, n)) + (0,)


length_multiplier = 1
n_phases = 100
for phase in range(1, n_phases + 1):
    signal_next = []
    for n in range(1, len(signal) + 1):
        pattern = make_pattern(n)
        sum = n_chars = 0
        signal_index = pattern_index = 0

        while n_chars < len(signal) * length_multiplier:
            sum += signal[signal_index] * pattern[pattern_index]
            n_chars += 1
            signal_index += 1
            if signal_index == len(signal):
                signal_index = 0
            pattern_index += 1
            if pattern_index == len(pattern):
                pattern_index = 0

        signal_next.append(abs(sum) % 10)

    signal = signal_next
print("After", phase, "phase:", ''.join(str(i) for i in signal[:8]))
