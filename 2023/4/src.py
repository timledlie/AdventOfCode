cards_count = {}
cards_matches = {}
card_number = 0
with open("input.txt") as file:
    for line in file.readlines():
        card_number += 1
        cards_count[card_number] = 1
        parts = line.strip().split(": ")
        winning_numbers, numbers_you_have = parts[1].split(" | ")
        winning_numbers = frozenset(winning_numbers.split())
        numbers_you_have = frozenset(numbers_you_have.split())
        num_winning_numbers = len(winning_numbers & numbers_you_have)
        cards_matches[card_number] = num_winning_numbers

num_cards_original = len(cards_count)
num_cards_total = 0
for card_id in range(1, len(cards_count) + 1):
    card_count = cards_count[card_id]
    card_matches = cards_matches[card_id]
    num_cards_total += card_count
    for i in range(card_id + 1, card_id + 1 + card_matches):
        if i > num_cards_original:
            break
        cards_count[i] += card_count

print(cards_count)
print(cards_matches)
print(num_cards_total)