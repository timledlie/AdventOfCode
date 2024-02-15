with open("input.txt") as file:
    signal = [int(el) for el in list(file.readline().strip())]

message_offset = int("".join([str(c) for c in signal[:7]]))
signal = (signal * 10000)[message_offset:]

n_phases = 100
for phase in range(1, n_phases + 1):
    signal_full_sum = sum(signal)
    signal_next = []
    for n in range(1, len(signal) + 1):
        signal_next.append(abs(signal_full_sum) % 10)
        signal_full_sum -= signal[n - 1]
    signal = signal_next
    print("After", phase, "phase:", ''.join(str(i) for i in signal[:8]))
