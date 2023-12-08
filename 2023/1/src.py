number_map_forwards = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9"
}

number_map_backwards = {}
for k, v in number_map_forwards.items():
    number_map_backwards[k[::-1]] = v


def translate_to_numbers(s, number_map):
    if len(s) == 0:
        return ""
    if s[0].isnumeric():
        return s[0] + translate_to_numbers(s[1:], number_map)
    for number_str, number_number in number_map.items():
        if s.startswith(number_str):
            return number_number + translate_to_numbers(s[len(number_str):], number_map)
    return translate_to_numbers(s[1:], number_map)


calibration_values_sum = 0
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()

        line_translated_forward = translate_to_numbers(line, number_map_forwards)
        line_translated_backward = translate_to_numbers(line[::-1], number_map_backwards)

        calibration_value = int(line_translated_forward[0] + line_translated_backward[0])
        calibration_values_sum += calibration_value

print(calibration_values_sum)
