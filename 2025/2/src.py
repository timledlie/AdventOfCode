with open("input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().split(",")]

sum_invalid_ids = 0
for a, b in ranges:
    for test_id in range(a, b + 1):
        test_id_str = str(test_id)
        len_test_id = len(test_id_str)
        if (len_test_id % 2 == 0) and (test_id_str[0:len_test_id//2] == test_id_str[len_test_id//2:]):
            sum_invalid_ids += test_id

print(sum_invalid_ids)
