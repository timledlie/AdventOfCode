from collections import namedtuple
from collections import defaultdict

card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def __lt__(self, other):
        for i in range(len(self.cards)):
            if card_values[self.cards[i]] < card_values[other.cards[i]]:
                return True
            elif card_values[self.cards[i]] > card_values[other.cards[i]]:
                return False
        return False

    def __eq__(self, other):
        return self.cards == other.cards

    def __repr__(self):
        return self.cards


def get_hand_type(cards):
    cards_dict = defaultdict(int)
    jokers = 0
    for card in cards:
        if card == "J":
            jokers += 1
        else:
            cards_dict[card] += 1

    if jokers:
        max_card, max_card_count = None, 0
        for card, card_count in cards_dict.items():
            if card_count > max_card_count:
                max_card_count = card_count
                max_card = card
        cards_dict[max_card] += jokers

    if len(cards_dict) == 1:
        return "five"
    if len(cards_dict) == 2:
        for card, count in cards_dict.items():
            if count == 4:
                return "four"
        return "full"
    if len(cards_dict) == 3:
        for card, count in cards_dict.items():
            if count == 3:
                return "three"
        return "two"
    if len(cards_dict) == 4:
        return "one"
    return "high"


hands = []
hands_by_type = defaultdict(list)
with open("input.txt") as file:
    for line in file.readlines():
        cards, bid = line.strip().split()
        hands_by_type[get_hand_type(cards)].append(Hand(cards, int(bid)))

for hand_type, hands in hands_by_type.items():
    hands_by_type[hand_type].sort()

rank = 1
total_winnings = 0
for hand_type in ("high", "one", "two", "three", "full", "four", "five"):
    for hand in hands_by_type[hand_type]:
        total_winnings += rank * hand.bid
        rank += 1
print(total_winnings)
