class Monkey:
    def __init__(self, items, operation_text, divisible_by, true_monkey, false_monkey):
        self.items = items
        self.operation_text = operation_text,
        self.operation_text = self.operation_text[0]
        self.divisible_by = divisible_by,
        self.divisible_by = self.divisible_by[0]
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0

    def has_items(self):
        return bool(self.items)

    def inspect(self):
        old = self.items[0]
        self.items[0] = eval(self.operation_text)
        self.items[0] = self.items[0] % 9699690
        self.inspect_count += 1

    def catch_item(self, item):
        self.items.append(item)

    def get_toss_recipient(self):
        return self.true_monkey if self.items[0] % self.divisible_by == 0 else self.false_monkey

    def toss_item(self, monkey):
        monkey.catch_item(self.items.pop(0))


def print_monkeys(monkeys: list):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        print("Monkey", i, "inspected items", monkey.inspect_count, "times.")
    print()


monkeys = []
with open("input.txt") as file:
    monkeys_text = file.read().split("\n\n")
    for monkey_text in monkeys_text:
        lines = monkey_text.split("\n")
        id = int(lines[0].split(' ')[1][0])
        starting_items = [int(n) for n in lines[1].split(": ")[1].split(', ')]
        operation_text = lines[2].split(" = ")[1]
        divisible_by = int(lines[3].split("divisible by ")[1])
        true_monkey = int(lines[4].split("to monkey ")[1])
        false_monkey = int(lines[5].split("to monkey ")[1])
        monkey = Monkey(
            starting_items,
            operation_text,
            divisible_by,
            true_monkey,
            false_monkey
        )
        monkeys.append(monkey)

for round in range(10000):
    for monkey in monkeys:
        for i in range(len(monkey.items)):
            monkey.inspect()
            monkey.toss_item(monkeys[monkey.get_toss_recipient()])
    print(round + 1)
    print_monkeys(monkeys)

inspect_counts = [m.inspect_count for m in monkeys]
inspect_counts.sort()
print(inspect_counts[-1] * inspect_counts[-2])