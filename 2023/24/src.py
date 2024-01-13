from sympy import nonlinsolve, symbols

# A line in three dimensions can be defined with three equations:
# x = x0 + at
# y = y0 + bt
# z = z0 + ct
# We throw our rock from (x, y, z) with velocity (a, b, c). Our rock's line must intersect the lines of the hailstones.
# We need three hailstones to be able to solve for (x, y, z).

u, v, w, a, b, c, x, y, z = symbols("u, v, w, a, b, c, x, y, z")
equations = []
with open("input.txt") as file:
    for t in (u, v, w):
        position_text, velocity_text = file.readline().strip().split("@")
        x0, y0, z0 = [int(c) for c in position_text.split(", ")]
        dx, dy, dz = [int(c) for c in velocity_text.split(", ")]
        equations.extend([
            x0 + dx * t - x - a * t,
            y0 + dy * t - y - b * t,
            z0 + dz * t - z - c * t,
        ])

result = set(nonlinsolve(equations, x, y, z, a, b, c, u, v, w)).pop()
print(result[0] + result[1] + result[2])
