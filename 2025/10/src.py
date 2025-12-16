import re
import itertools
from collections import namedtuple

MachineDefinition = namedtuple('MachineDefinition', ['lights', 'buttons'])

machine_definitions = []
with (open("input.txt") as f):
    for line in f.readlines():
        lights = re.search(r"\[(.*?)\]", line).group(1)
        button_matches = re.findall(r"\((.*?)\)", line)
        buttons = [
            tuple(int(x) for x in b.split(","))
            for b in button_matches
        ]
        machine_definitions.append(MachineDefinition(lights, buttons))


def find_min_presses_to_configure(lights_goal, buttons_options):
    for n_presses in range(1, len(buttons_options) + 1):
        for button_presses in itertools.combinations(buttons_options, n_presses):
            lights = list('.' * len(lights_goal))
            for buttons in button_presses:
                for b in buttons:
                    if lights[b] == '.':
                        lights[b] = '#'
                    else:
                        lights[b] = '.'
            if ''.join(lights) == lights_goal:
                return n_presses
    return None

print(sum([find_min_presses_to_configure(md.lights, md.buttons) for md in machine_definitions]))
