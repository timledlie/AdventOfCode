class Node:
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous
        self.next = None


def print_nodes(starting_from, n):
    for i in range(n):
        print(starting_from.value, end=', ')
        starting_from = starting_from.next
    print()


decryption_key = 811589153
with open("input.txt") as file:
    numbers = [811589153 * int(n) for n in file.readlines()]
    # numbers = [int(n) for n in file.readlines()]

previous = None
all_nodes = []
zero_node = None
for number in numbers:
    node = Node(number, previous)
    if previous:
        previous.next = node
    previous = node
    if number == 0:
        zero_node = node
    all_nodes.append(node)

all_nodes[0].previous = all_nodes[-1]
all_nodes[-1].next = all_nodes[0]
n_nodes = len(all_nodes)

for i in range(10):
    for node in all_nodes:
        if node.value % len(all_nodes) == 0:
            continue

        prev, next = node.previous, node.next

        node.previous.next = node.next
        node.next.previous = node.previous

        if node.value > 0:
            pointer = next
            for i in range((node.value - 1) % (n_nodes - 1)):
                pointer = pointer.next
        elif node.value < 0:
            pointer = prev
            for i in range(abs(node.value) % (n_nodes - 1)):
                pointer = pointer.previous

        node.previous = pointer
        node.next = pointer.next
        pointer.next.previous = node
        pointer.next = node

grove_sum = 0
pointer = zero_node
for i in range(3):
    for j in range(1000):
        pointer = pointer.next
    grove_sum += pointer.value
print(grove_sum)
