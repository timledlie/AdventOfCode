with open("input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().split(",")]

sum_invalid_ids = 0
for a, b in ranges:
    for test_id in range(a, b + 1):
        test_id_str = str(test_id)
        len_test_id = len(test_id_str)
        for repeat_length in range(1, len_test_id // 2 + 1):
            if test_id_str == test_id_str[:repeat_length] * (len_test_id // repeat_length):
                sum_invalid_ids += test_id
                break

print(sum_invalid_ids)
