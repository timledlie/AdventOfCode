import re
from collections import defaultdict

max_coord = 4000000
row_spans = defaultdict(list)  # y: [(s, e), (s, e), ...]
with open("input.txt") as file:
    for line in file.readlines():
        m1 = re.search('Sensor at x=(.+?),', line)
        m2 = re.search(', y=(.+?): closest', line)
        m3 = re.search('closest beacon is at x=(.+?),', line)
        m4 = re.search(', y=(.+?);', line.strip()[20:] + ";")
        sensor = (int(m1.group(1)), int(m2.group(1)))
        beacon = (int(m3.group(1)), int(m4.group(1)))

        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        for y in range(-1 * distance, distance + 1):
            row_spans[sensor[1] + y].append((sensor[0] - (distance - abs(y)), sensor[0] + (distance - abs(y))))


def overlapping_pair(spans):
    for i in range(len(spans) - 1):
        a = spans[i]
        for j in range(i + 1, len(spans)):
            b = spans[j]
            if a[0] <= b[0] and a[1] >= b[1]:
                return spans[i], spans[j], a
            if b[0] <= a[0] and b[1] >= a[1]:
                return spans[i], spans[j], b
            if a[0] - 1 <= b[1] <= a[1]:
                return spans[i], spans[j], (b[0], a[1])
            if a[0] <= b[0] <= a[1] + 1:
                return spans[i], spans[j], (a[0], b[1])

    return None, None, None


for y in range(max_coord + 1):
    spans = row_spans[y]
    while True:
        if len(spans) < 2:
            break
        s1, s2, combined = overlapping_pair(spans)
        if combined is None:
            if len(spans) == 2:
                print(y, spans)
                break
        spans.remove(s1)
        spans.remove(s2)
        spans.append(combined)
