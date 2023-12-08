# f: open("input_sample.txt", "r")
# depths: [int(str(d).strip()) for d in f.readlines()]
# import numpy as np
# import statistics
from collections import defaultdict
# import math
# from collections import namedtuple
# from collections import deque
# PasswordCheck = namedtuple('PasswordCheck', ['span', 'letter', 'password'])
# import re
# from itertools import combinations
# import copy

allergens_map = defaultdict(list)
ingredients_count = defaultdict(int)
with open("input.txt") as file:
    for line in file.readlines():
        ingredients, allergens = line.split('(')
        ingredients = set(ingredients.strip().split())
        allergens = allergens.strip()[9:-1].split(', ')
        for allergen in allergens:
            allergens_map[allergen].append(ingredients)
        for ingredient in ingredients:
            ingredients_count[ingredient] += 1
print(allergens_map)
print(ingredients_count)

for allergen, ingredients_sets in allergens_map.items():
    allergens_map[allergen] = set.intersection(*ingredients_sets)

print(allergens_map)


def ambiguous(allergens_map):
    for ingredients in allergens_map.values():
        if len(ingredients) > 1:
            return True
    return False


known_allergic_ingredients = {}
while ambiguous(allergens_map):
    for allergen, ingredients in allergens_map.items():
        if len(ingredients) == 1:
            known_allergic_ingredients[allergen] = list(ingredients)[0]
        else:
            for known_ingredient in known_allergic_ingredients.values():
                if known_ingredient in ingredients:
                    ingredients.remove(known_ingredient)
print(known_allergic_ingredients)
print(allergens_map)

allergic_ingredients = []
for allergen_list in allergens_map.values():
    allergic_ingredients += allergen_list
print(allergic_ingredients)

total_ingredients_count = 0
allergic_ingredient_count = 0
for ingredient, ingredient_count in ingredients_count.items():
    total_ingredients_count += ingredient_count
    if ingredient in allergic_ingredients:
        allergic_ingredient_count += ingredient_count
print(total_ingredients_count, allergic_ingredient_count, total_ingredients_count - allergic_ingredient_count)

print(allergens_map)
allergens = list(allergens_map.keys())
allergens.sort()
print(allergens)
canonical_dangerous_ingredient_list = ''
for allergen in allergens:
    canonical_dangerous_ingredient_list += list(allergens_map[allergen])[0] + ','
print(canonical_dangerous_ingredient_list)