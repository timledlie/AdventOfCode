reports = []
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        reports.append([int(level) for level in line.split()])


def is_report_safe(report):
    is_increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        a, b = report[i], report[i + 1]
        if abs(a - b) > 3:
            return False
        if a == b:
            return False
        if is_increasing and (a > b):
            return False
        if not is_increasing and (a < b):
            return False

    return True


def is_report_almost_safe(report):
    for i in range(len(report)):
        if is_report_safe(report[:i] + report[i+1:]):
            return True
    return False


count_safe = 0
for report in reports:
    if is_report_almost_safe(report):
        count_safe += 1

print(count_safe)
