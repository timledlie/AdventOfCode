class Workflow:
    def __init__(self, rules):
        self.rules = rules


class Rule:
    def __init__(self, part_category, operation, value, part_destination):
        self.part_category = part_category
        self.operation = operation
        self.value = value
        self.part_destination = part_destination


class PartRating:
    def __init__(self, ratings_dict):
        self.ratings_dict = ratings_dict

    def get_value(self):
        return self.ratings_dict["x"] + self.ratings_dict["m"] + self.ratings_dict["a"] + self.ratings_dict["s"]


def is_rule_passes(part_rating, rule):
    if rule.operation == ">":
        return part_rating.ratings_dict[rule.part_category] > rule.value
    return part_rating.ratings_dict[rule.part_category] < rule.value


def is_part_accepted(part_rating, workflows):
    state = "in"
    while True:
        workflow = workflows[state]
        for rule in workflow.rules:
            if is_rule_passes(part_rating, rule):
                state = rule.part_destination
                if state == "A":
                    return True
                if state == "R":
                    return False
                break
    exit("poop")


workflows = {}
part_ratings = []
with open("input.txt") as file:
    text = file.read()

workflows_text, part_ratings_text = text.strip().split("\n\n")

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

part_ratings = []
for part_ratings_line in part_ratings_text.split("\n"):
    ratings_dict = {}
    for part_rating in part_ratings_line[1:-1].split(","):
        part_category, value = part_rating.split("=")
        ratings_dict[part_category] = int(value)
    part_ratings.append(PartRating(ratings_dict))

accepted_total = 0
for part_rating in part_ratings:
    if is_part_accepted(part_rating, workflows):
        accepted_total += part_rating.get_value()

print(accepted_total)
