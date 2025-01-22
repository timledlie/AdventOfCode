import collections

with open("input.txt") as file:
    initial_secret_numbers = [int(line.strip()) for line in file.readlines()]

rounds = 2000
running_sum = 0
all_last_4_scores = []
all_last_4_steps = set()
for n in initial_secret_numbers:
    last_n_mod_10 = n % 10
    last_4_diffs = collections.deque([], 4)
    last_4_scores = {}
    for r in range(rounds):
        m = n * 64
        n = m ^ n
        n = n % 16777216

        m = n // 32
        n = m ^ n
        n = n % 16777216

        m = n * 2048
        n = m ^ n
        n = n % 16777216

        n_mod_10 = n % 10
        last_4_diffs.append(n_mod_10 - last_n_mod_10)
        if len(last_4_diffs) == 4:
            tuple_last_4_diffs = tuple(last_4_diffs)
            all_last_4_steps.add(tuple_last_4_diffs)
            if tuple_last_4_diffs not in last_4_scores:
                last_4_scores[tuple_last_4_diffs] = n_mod_10
        last_n_mod_10 = n_mod_10
    all_last_4_scores.append(last_4_scores)

best_score = 0
for sequence in all_last_4_steps:
    score_sum = 0
    for last_4_scores in all_last_4_scores:
        if sequence in last_4_scores:
            score_sum += last_4_scores[sequence]
    if score_sum > best_score:
        best_score = score_sum

print(best_score)
