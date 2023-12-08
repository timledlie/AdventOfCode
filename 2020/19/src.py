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
    file_contents = file.read()

parts = file_contents.split("\n\n")
rules_block = parts[0]

messages = set([m for m in parts[1].split()])
messages_chunked = []
for message in messages:
    messages_chunked.append([message[i:i + 8] for i in range(0, len(message), 8)])

rules_lines = rules_block.split("\n")
rules = {}
simple_rule_ids = set()
complex_rule_ids = set()
for rules_line in rules_lines:
    parts = rules_line.split(': ')
    left_side = parts[0]
    right_side = parts[1]
    if right_side == '"a"':
        rules[left_side] = set(['a'])
        simple_rule_ids.add(left_side)
    elif right_side == '"b"':
        rules[left_side] = set(['b'])
        simple_rule_ids.add(left_side)
    else:
        rules[left_side] = right_side
        complex_rule_ids.add(left_side)
print(rules)
print(simple_rule_ids)
print(complex_rule_ids)


def convert_rule_to_number_set(rule):
    if '|' in rule:
        rule = rule.replace('|', '')
    return set(rule.split())


def convert_rule_to_letters(rule):
    if '|' not in rule:
        if ' ' not in rule:
            return rules[rule]
        else:
            options = set()
            rule_ids = rule.split()
            if len(rule_ids) == 2:
                for option_first in rules[rule_ids[0]]:
                    for option_second in rules[rule_ids[1]]:
                        options.add(option_first + option_second)
            else:
                for option_first in rules[rule_ids[0]]:
                    for option_second in rules[rule_ids[1]]:
                        for option_third in rules[rule_ids[2]]:
                            options.add(option_first + option_second + option_third)
            return options
    else:
        alternatives = rule.split(' | ')
        options = set()
        if ' ' not in alternatives[0]:
            options = rules[alternatives[0]] | rules[alternatives[1]]
        else:
            rule_ids_0 = alternatives[0].split()
            rule_ids_1 = alternatives[1].split()
            for option_first in rules[rule_ids_0[0]]:
                for option_second in rules[rule_ids_0[1]]:
                    options.add(option_first + option_second)
            if len(rule_ids_1) == 2:
                for option_first in rules[rule_ids_1[0]]:
                    for option_second in rules[rule_ids_1[1]]:
                        options.add(option_first + option_second)
            else:
                for option_first in rules[rule_ids_1[0]]:
                    for option_second in rules[rule_ids_1[1]]:
                        for option_third in rules[rule_ids_1[2]]:
                            options.add(option_first + option_second + option_third)
        return options


while complex_rule_ids:
    for complex_rule_id in complex_rule_ids:
        number_set = convert_rule_to_number_set(rules[complex_rule_id])
        if len(number_set - simple_rule_ids) == 0:
            rules[complex_rule_id] = convert_rule_to_letters(rules[complex_rule_id])
            break
    simple_rule_ids.add(complex_rule_id)
    complex_rule_ids.remove(complex_rule_id)

matching_messages = messages & rules['0']
print("We started with", len(messages), "messages")
print(len(matching_messages), "of them matched via initial rules")

print(rules['8'])
print(rules['11'])
print(rules['42'])
print(rules['31'])
unit_length = len(next(iter(rules['42'])))

messages_chunked = {}
for message in messages:
    messages_chunked[message] = [message[i:i + unit_length] for i in range(0, len(message), unit_length)]

patterns_42 = rules['42']
patterns_31 = rules['31']
for message, message_chunks in messages_chunked.items():
    chunk_count = len(message_chunks)
    is_matching_42s = True
    match_count_42 = 0
    match_count_31 = 0
    for chunk in message_chunks:
        if is_matching_42s:
            if chunk in patterns_42:
                match_count_42 += 1
            else:
                is_matching_42s = False
        if not is_matching_42s:
            if chunk in patterns_31:
                match_count_31 += 1
    if (match_count_42 + match_count_31 == chunk_count) and (match_count_42 > match_count_31) and (match_count_31 > 0):
        matching_messages.add(message)

print("After chunk processing, we have", len(matching_messages), "total matching")
for m in matching_messages:
    print(m)