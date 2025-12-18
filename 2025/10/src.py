import re
from collections import namedtuple
from collections import defaultdict
import pulp

MachineDefinition = namedtuple('MachineDefinition', ['buttons', 'joltages'])

machine_definitions = []
with (open("input.txt") as f):
    for line in f.readlines():
        joltages = tuple(map(int, re.search(r"\{(.*?)\}", line).group(1).split(',')))
        button_matches = re.findall(r"\((.*?)\)", line)
        buttons = [
            tuple(int(x) for x in b.split(","))
            for b in button_matches
        ]
        machine_definitions.append(MachineDefinition(buttons, joltages))


# Model the problem as a system of linear equations while minimize the sum of the variables.
#
# For example:
# buttons: (3) (1,3) (2) (2,3) (0,2) (0,1)
#           v0  v1    v2  v3    v4    v5
# joltages: {3,5,4,7}
#
# This produces the following system of equations:
# v4 + v5      = 3  (we need to press buttons v4 and v5 a total of 3 times)
# v1 + v5      = 5
# v2 + v3 + v4 = 4
# v0 + v1 + v3 = 7
#
# We find the positive, integer solutions to this system that minimizes the sum of the variables.
def find_min_presses_to_configure(buttons_options, joltages_goal):
    variables = [pulp.LpVariable("v" + str(i), lowBound=0, cat="Integer") for i in range(len(buttons_options))]

    model = pulp.LpProblem("Integer_Equation_System", pulp.LpMinimize)
    model += pulp.lpSum(variables)

    equations = defaultdict(list)
    for i in range(len(buttons_options)):
        for button in buttons_options[i]:
            equations[button].append(i)

    for joltage_index, var_ids in equations.items():
        model += pulp.lpSum([variables[i] for i in var_ids]) == joltages_goal[joltage_index]

    model.solve(pulp.PULP_CBC_CMD(msg=False))
    return int(pulp.value(model.objective))


print(sum([find_min_presses_to_configure(md.buttons, md.joltages) for md in machine_definitions]))
