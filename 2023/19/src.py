class Workflow:
    def __init__(self, rules):
        self.rules = rules

    def __repr__(self):
        return ", ".join([rule.__repr__() for rule in self.rules])


class Rule:
    def __init__(self, part_category, operation, value, part_destination):
        self.part_category = part_category
        self.operation = operation
        self.value = value
        self.part_destination = part_destination

    def __repr__(self):
        return self.part_category + " " + self.operation + " " + str(self.value) + ": " + self.part_destination


workflows = {}
with open("input.txt") as file:
    text = file.read()

workflows_text = text.strip().split("\n\n")[0]

for workflow_line in workflows_text.split("\n"):
    name, rest = workflow_line.split("{")
    rules_text = rest[:-1].split(",")
    default = rules_text[-1]
    rules = []
    for rule_text in rules_text[:-1]:
        parts = rule_text.split(":")
        part_destination = parts[1]
        part_category, operation, value = parts[0][0], parts[0][1], int(parts[0][2:])
        rules.append(Rule(part_category, operation, value, part_destination))
    rules.append(Rule("x", ">", 0, default))  # the default is a rule that is always True
    workflows[name] = Workflow(rules)


def find_accepted_paths(node):
    if node == "A":
        return [[("x", ">", 0)]]
    if node == "R":
        return None

    prerequisites = []
    permutations = []
    for rule in workflows[node].rules:
        rule_pass = (rule.part_category, rule.operation, rule.value)
        recursion_permutations = find_accepted_paths(rule.part_destination)
        if recursion_permutations is not None:
            permutations += [prerequisites + [rule_pass] + p for p in recursion_permutations]

        if rule.operation == "<":
            fail_operation = ">="
        else:
            fail_operation = "<="
        rule_fail = (rule.part_category, fail_operation, rule.value)
        prerequisites.append(rule_fail)

    return permutations


combinations = 0
max_default = 4000
paths = find_accepted_paths("in")
for path in paths:
    mins = {"x": 1, "m": 1, "a": 1, "s": 1}
    maxes = {"x": max_default, "m": max_default, "a": max_default, "s": max_default}
    for category, operation, value in path:
        if operation == "<":
            if maxes[category] >= value:
                maxes[category] = value - 1
        elif operation == "<=":
            if maxes[category] > value:
                maxes[category] = value
        elif operation == ">":
            if mins[category] <= value:
                mins[category] = value + 1
        elif operation == ">=":
            if mins[category] < value:
                mins[category] = value
    product = 1
    for category in ("x", "m", "a", "s"):
        n_permutations = maxes[category] - mins[category] + 1
        if n_permutations < 0:
            n_permutations = 0
        product *= n_permutations
    combinations += product
print(combinations)
