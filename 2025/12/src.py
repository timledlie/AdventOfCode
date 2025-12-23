# When researching "bin packing" algorithms, I found
# https://stackoverflow.com/questions/47918792/2d-bin-packing-on-a-grid
# which was very relevant and started me investigating modeling this problem as a boolean satisfiability problem.
# Then I used ChatGPT to show me how to use PySAT for a problem like this. But before I started implementing,
# I asked ChatGPT if PySAT would scale for larger grids, and it said "no" and recommended I try Google's OR-Tools.
# ChatGPT wrote most of the code below. It takes about 40 minutes to complete on my computer.

from collections import namedtuple
from ortools.sat.python import cp_model

TreeSpec = namedtuple('TreeSpec', ('width', 'length', 'shape_quantities'))

with (open("input.txt") as f):
    file_lines = f.readlines()

PRESENT_SHAPES = {}
for i in range(6):
    shape = set()
    for r in range(3):
        for c in range(3):
            if file_lines[i * 5 + 1 + r][c] == '#':
                shape.add((r, c))
    PRESENT_SHAPES[i] = frozenset(shape)

tree_specs = []
for line in file_lines[30:]:
    regions_text, shape_quantities_text = line.split(':')
    width, length = tuple(map(int, regions_text.split('x')))
    shape_quantities = dict(enumerate(list(map(int, shape_quantities_text.strip().split()))))
    tree_specs.append(TreeSpec(width, length, shape_quantities))

def normalize(shape):
    min_r = min(r for r, _ in shape)
    min_c = min(c for _, c in shape)
    return frozenset((r - min_r, c - min_c) for r, c in shape)

def rotate(shape):
    return {(c, -r) for r, c in shape}

def reflect(shape):
    return {(r, -c) for r, c in shape}

def all_orientations(shape):
    result = set()
    cur = shape
    for _ in range(4):
        cur = rotate(cur)
        result.add(normalize(cur))
        result.add(normalize(reflect(cur)))
    return result

def generate_all_possible_placements(width, length, shape):
    placements = []
    for oriented in all_orientations(shape):
        max_r = max(r for r, _ in oriented)
        max_c = max(c for _, c in oriented)
        for r0 in range(width - max_r):
            for c0 in range(length - max_c):
                cells = frozenset((r0 + r, c0 + c) for r, c in oriented)
                placements.append(cells)
    return placements

def is_tiling_feasible(tree_spec):
    shape_area = {s: len(cells) for s, cells in PRESENT_SHAPES.items()}

    total_required_area = sum(tree_spec.shape_quantities[s] * shape_area[s] for s in PRESENT_SHAPES)
    grid_area = tree_spec.width * tree_spec.length

    return grid_area >= total_required_area

def placement_exists(tree_spec):
    if not is_tiling_feasible(tree_spec):
        return False

    placements = {}
    for s, shape in PRESENT_SHAPES.items():
        placements[s] = generate_all_possible_placements(tree_spec.width, tree_spec.length, shape)

    model = cp_model.CpModel()

    # one variable for each possible present placement
    vars = {}
    for s in placements:
        for p in range(len(placements[s])):
            vars[(s, p)] = model.NewBoolVar(f"x_{s}_{p}")

    # presents can not overlap each other (no one cell can have more than one present covering it)
    cell_to_vars = {}
    for (s, p), var in vars.items():
        for cell in placements[s][p]:
            cell_to_vars.setdefault(cell, []).append(var)
    for vlist in cell_to_vars.values():
        model.Add(sum(vlist) <= 1)

    # present count constraints
    for s in placements:
        model.Add(
            sum(vars[(s, p)] for p in range(len(placements[s]))) == tree_spec.shape_quantities[s]
        )

    # Solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 60
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    return status in (cp_model.FEASIBLE, cp_model.OPTIMAL)


print(sum([placement_exists(ts) for ts in tree_specs]))
