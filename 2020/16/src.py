# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
from collections import defaultdict
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
# from copy import deepcopy


with open("input.txt") as file:
    (ranges, your_ticket, nearby_tickets_text) = file.read().split("\n\n")
ranges = ranges.split("\n")
your_ticket = your_ticket.split("\n")
nearby_tickets_components = nearby_tickets_text.split("\n")

your_ticket = your_ticket[1]
your_ticket = [int(n) for n in your_ticket.split(',')]

ticket_field_rules = {}
for ranges_text in ranges:
    parts = ranges_text.split(': ')
    ticket_field = parts[0]
    parts = parts[1].split(' or ')

    valid_numbers = set()
    number_range = parts[0].split('-')
    for number_range in parts:
        start, end = number_range.split('-')
        for n in range(int(start), int(end) + 1):
            valid_numbers.add(n)

    ticket_field_rules[ticket_field] = valid_numbers

all_valid_numbers = set()
for number_list in ticket_field_rules.values():
    for number in number_list:
        all_valid_numbers.add(number)

nearby_tickets_components.pop(0)
nearby_tickets = defaultdict(set)
nearby_tickets_components = [part.split(',') for part in nearby_tickets_components]
for nearby_ticket in nearby_tickets_components:
    skip = False
    for number in nearby_ticket:
        if int(number) not in all_valid_numbers:
            skip = True
    if not skip:
        for i in range(len(nearby_ticket)):
            nearby_tickets[i].add(int(nearby_ticket[i]))
    else:
        print("Skipping", nearby_ticket)

print(your_ticket)
print(ticket_field_rules)
print(nearby_tickets)

answer = {}
map_index_to_field = {}
while len(nearby_tickets) > 0:
    for ticket_index, ticket_numbers in nearby_tickets.items():
        count_matches = 0
        for ticket_field, ticket_field_numbers in ticket_field_rules.items():
            if ticket_numbers & ticket_field_numbers == ticket_numbers:
                count_matches += 1
                ticket_index_match = ticket_index
                ticket_field_match = ticket_field
                answer[ticket_index] = ticket_field
        if count_matches == 1:
            break
    del nearby_tickets[ticket_index_match]
    del ticket_field_rules[ticket_field_match]

print(answer)
product = 1
for index, ticket_field in answer.items():
    if "departure" in ticket_field:
        product *= your_ticket[index]
print(product)