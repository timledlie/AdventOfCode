# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
# from collections import defaultdict
# import math
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
# import copy

# with open("input.txt") as file:
#     file_text = file.read()

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


def run_simulation(cups, total_cups, n_moves):
    for move in range(1, n_moves + 1):
        # print(move, cups)
        current_cup = cups[0]
        removed_cups = cups[1:4]
        destination_cup = current_cup - 1
        if destination_cup == 0:
            destination_cup = total_cups
        while destination_cup in removed_cups:
            destination_cup -= 1
            if destination_cup == 0:
                destination_cup = total_cups
        destination_index = cups.index(destination_cup)
        cups = cups[4:destination_index] + [destination_cup] + removed_cups + cups[destination_index + 1:] + [current_cup]

    one_index = cups.index(1)
    if one_index == total_cups - 2:
        after_one = [cups[-1], cups[0]]
    elif one_index == total_cups - 1:
        after_one = [cups[0], cups[1]]
    else:
        after_one = cups[one_index + 1:one_index + 3]
    return after_one


def run_simulation_linked_list(current, pointers, n_moves, total_cups):
    for move in range(1, n_moves + 1):
        # print(move)
        # print_circular_linked_list(current)
        next1, next2, next3 = current.next, current.next.next, current.next.next.next
        # print("pick up:", next1, next2, next3)
        destination_cup_value = current.data - 1
        if destination_cup_value == 0:
            destination_cup_value = total_cups
        while destination_cup_value in (next1.data, next2.data, next3.data):
            destination_cup_value -= 1
            if destination_cup_value == 0:
                destination_cup_value = total_cups
        current.next = next3.next
        destination_cup = pointers[destination_cup_value]
        next3.next = destination_cup.next
        destination_cup.next = next1
        current = current.next
    one_after_one = pointers[1].next.data
    two_after_one = pointers[1].next.next.data
    print(one_after_one, two_after_one, one_after_one * two_after_one)


def print_circular_linked_list(head):
    head_orig = head
    while True:
        print(head, "", end='')
        head = head.next
        if head == head_orig:
            break
    print()


def construct_circular_linked_list(seed, total_cups):
    pointers = {}
    cups = [int(c) for c in list(seed[::-1])]
    next = None
    end = None
    for n in range(total_cups, 9, -1):
        node = Node(n, next)
        if end is None:
            end = node
        pointers[n] = node
        next = node
    for n in cups:
        node = Node(n, next)
        if end is None:
            end = node
        pointers[n] = node
        next = node
    current = node
    end.next = node
    return current, pointers


total_cups = 1000000
n_moves = 10000000
seed = '158937462'

# cups = [int(c) for c in list(seed[::-1])]
# cups += range(10, total_cups + 1)

current, pointers = construct_circular_linked_list(seed, total_cups)
orig_current = current
run_simulation_linked_list(current, pointers, n_moves, total_cups)