import re
from collections import namedtuple
from collections import defaultdict
import copy
import datetime

Blueprint = namedtuple("Blueprint", ("id", "ore_ore", "clay_ore", "obsidian_ore", "obsidian_clay", "geode_ore", "geode_obsidian"))

blueprints = []
with open("input.txt") as file:
    for line in file.readlines():
        m = re.search('Blueprint (.+?): Each ore robot costs (.+?) ore. Each clay robot costs (.+?) ore. Each obsidian robot costs (.+?) ore and (.+?) clay. Each geode robot costs (.+?) ore and (.+?) obsidian.', line)
        blueprints.append(Blueprint(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)), int(m.group(7))))


def add_new_inventory(inventory, new_inventory):
    sum_inventory = defaultdict(int)
    for element in ('ore', 'clay', 'obsidian', 'geode'):
        sum_inventory[element] = inventory[element] + new_inventory[element]
    return sum_inventory


memo = {}
def max_geode_count(blueprint, current_minute, inventory, robots, robots_to_skip):
    if current_minute == 33:
        return inventory['geode']

    fingerprint = (blueprint, current_minute, tuple(inventory.items()), tuple(robots.items()))
    if fingerprint in memo:
        return memo[fingerprint]

    new_inventory = defaultdict(int)
    for robot_name, robot_count in robots.items():
        new_inventory[robot_name] += robot_count

    count_build_ore, count_build_clay, count_build_obsidian, count_build_geode, count_build_none = 0, 0, 0, 0, 0
    robots_to_skip_cur = set()
    for robot_to_build in ('ore', 'clay', 'obsidian', 'geode', 'none'):
        robots_copy = copy.copy(robots)
        inventory_copy = copy.copy(inventory)
        if robot_to_build == 'ore' and (inventory['ore'] >= blueprint.ore_ore) and ('ore' not in robots_to_skip):
            robots_to_skip_cur.add('ore')
            robots_copy['ore'] += 1
            inventory_copy['ore'] -= blueprint.ore_ore
            count_build_ore = max_geode_count(blueprint, current_minute + 1, add_new_inventory(inventory_copy, new_inventory), robots_copy, {})
        elif robot_to_build == 'clay' and (inventory['ore'] >= blueprint.clay_ore) and ('clay' not in robots_to_skip):
            robots_to_skip_cur.add('clay')
            robots_copy['clay'] += 1
            inventory_copy['ore'] -= blueprint.clay_ore
            count_build_clay = max_geode_count(blueprint, current_minute + 1, add_new_inventory(inventory_copy, new_inventory), robots_copy, {})
        elif robot_to_build == 'obsidian' and (inventory['ore'] >= blueprint.obsidian_ore) and (inventory['clay'] >= blueprint.obsidian_clay) and ('obsidian' not in robots_to_skip):
            robots_to_skip_cur.add('obsidian')
            robots_copy['obsidian'] += 1
            inventory_copy['ore'] -= blueprint.obsidian_ore
            inventory_copy['clay'] -= blueprint.obsidian_clay
            count_build_obsidian = max_geode_count(blueprint, current_minute + 1, add_new_inventory(inventory_copy, new_inventory), robots_copy, {})
        elif robot_to_build == 'geode' and (inventory['ore'] >= blueprint.geode_ore) and (inventory['obsidian'] >= blueprint.geode_obsidian) and ('geode' not in robots_to_skip):
            robots_to_skip_cur.add('geode')
            robots_copy['geode'] += 1
            inventory_copy['ore'] -= blueprint.geode_ore
            inventory_copy['obsidian'] -= blueprint.geode_obsidian
            count_build_geode = max_geode_count(blueprint, current_minute + 1, add_new_inventory(inventory_copy, new_inventory), robots_copy, {})
        elif robot_to_build == 'none':
            count_build_none = max_geode_count(blueprint, current_minute + 1, add_new_inventory(inventory_copy, new_inventory), robots_copy, robots_to_skip_cur)

    result = max(count_build_ore, count_build_clay, count_build_obsidian, count_build_geode, count_build_none)
    memo[fingerprint] = result
    return result


total_quality = 0
print(datetime.datetime.now())
for blueprint in blueprints[1:3]:
    inventory = defaultdict(int)
    robots = defaultdict(int)
    robots['ore'] = 1
    answer = max_geode_count(blueprint, 1, inventory, robots, {})
    total_quality += blueprint.id * answer
    print(blueprint.id, answer, datetime.datetime.now())
print(total_quality)
