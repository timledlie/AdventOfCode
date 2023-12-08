import copy


class Monkey:
    def __init__(self, name):
        self.name = name
        self.value = None


monkeys = {}
with open("input.txt") as file:
    for line in file.readlines():
        parts = line.strip().split(': ')
        name = parts[0]
        monkey = Monkey(name)
        if len(parts[1]) > 4:
            left, operation, right = parts[1].split(' ')
            monkey.left, monkey.operation, monkey.right = parts[1].split(' ')
        else:
            monkey.value = int(parts[1])
        monkeys[name] = monkey


def doit(monkeys):
    while True:
        for monkey in monkeys.values():
            if monkey.value is None:
                left, right = monkeys[monkey.left].value, monkeys[monkey.right].value
                if (left is not None) and (right is not None):
                    if (monkey.name == 'root'):
                        print(left, " = ", right)
                        return
                    if monkey.operation == '+':
                        if isinstance(left, int) and isinstance(right, int):
                            monkey.value = left + right
                        else:
                            monkey.value = " (" + str(left) + " " + monkey.operation + " " + str(right) + ") "
                    elif monkey.operation == '-':
                        if isinstance(left, int) and isinstance(right, int):
                            monkey.value = left - right
                        else:
                            monkey.value = " (" + str(left) + " " + monkey.operation + " " + str(right) + ") "
                    elif monkey.operation == '*':
                        if isinstance(left, int) and isinstance(right, int):
                            monkey.value = left * right
                        else:
                            monkey.value = " (" + str(left) + " " + monkey.operation + " " + str(right) + ") "
                    elif monkey.operation == '/':
                        if isinstance(left, int) and isinstance(right, int):
                            monkey.value = left // right
                        else:
                            monkey.value = " (" + str(left) + " " + monkey.operation + " " + str(right) + ") "


monkeys["humn"].value = "x"
doit(monkeys)