import itertools

class Moon:
    def __init__(self, position: list):
        self.position = position
        self.velocity = [0, 0, 0]

    def apply_gravity(self, other_moon):
        for axis in range(3):
            if self.position[axis] < other_moon.position[axis]:
                self.velocity[axis] += 1
            elif self.position[axis] > other_moon.position[axis]:
                self.velocity[axis] -= 1

    def apply_velocity(self):
        for axis in range(3):
            self.position[axis] += self.velocity[axis]

    def total_energy(self):
        potential_energy = kinetic_energy = 0
        for pos in self.position:
            potential_energy += abs(pos)
        for vel in self.velocity:
            kinetic_energy += abs(vel)
        return potential_energy * kinetic_energy


def system_enery(moons):
    total = 0
    for moon in moons:
        total += moon.total_energy()
    return total


def averages(moons):
    positions = [0, 0, 0]
    velocities = [0, 0, 0]
    for moon in moons:
        for axis in range(3):
            positions[axis] += moon.position[axis]
            velocities[axis] += moon.velocity[axis]
    return [[positions[0] / 4, positions[1] / 4, positions[2] / 4],
            [velocities[0] / 4, velocities[1] / 4, velocities[2] / 4]]


def print_moons(moons):
    for moon in moons:
        print(f'{moon.position[0]:>4}', f'{moon.position[1]:>4}', f'{moon.position[2]:>4}', sep=', ', end=' ')
        print(f'{moon.velocity[0]:>4}', f'{moon.velocity[1]:>4}', f'{moon.velocity[2]:>4}', sep=', ', end=' || ')
    print()


def get_sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


n = 0
for i in range(4686774924):
    n = 1
print(n)
exit()


moons = []
with open("input_sample.txt") as file:
    for line in file.readlines():
        parts = line.split('=')
        x = int(parts[1].split(',')[0])
        y = int(parts[2].split(',')[0])
        z = int(parts[3].split('>')[0])
        moons.append(Moon([x, y, z]))

ab = [moons[0].position[0] - moons[1].position[0], moons[0].position[1] - moons[1].position[1], moons[0].position[2] - moons[1].position[2]]
ac = [moons[0].position[0] - moons[2].position[0], moons[0].position[1] - moons[2].position[1], moons[0].position[2] - moons[2].position[2]]
ad = [moons[0].position[0] - moons[3].position[0], moons[0].position[1] - moons[3].position[1], moons[0].position[2] - moons[3].position[2]]
bc = [moons[1].position[0] - moons[2].position[0], moons[1].position[1] - moons[2].position[1], moons[1].position[2] - moons[2].position[2]]
bd = [moons[1].position[0] - moons[3].position[0], moons[1].position[1] - moons[3].position[1], moons[1].position[2] - moons[3].position[2]]
cd = [moons[2].position[0] - moons[3].position[0], moons[2].position[1] - moons[3].position[1], moons[2].position[2] - moons[3].position[2]]

va = moons[0].velocity
vb = moons[1].velocity
vc = moons[2].velocity
vd = moons[3].velocity

for step in range(4686774926):
    if va == [0, 0, 0] and vb == [0, 0, 0] and vc == [0, 0, 0] and vd == [0, 0, 0]:
        print("after", f'{step:>3}', "steps ", ab, ac, ad, bc, bd, cd)

    for axis in range(3):
        s = get_sign(ab[axis])
        va[axis] -= s
        vb[axis] += s
        s = get_sign(ac[axis])
        va[axis] -= s
        vc[axis] += s
        s = get_sign(ad[axis])
        va[axis] -= s
        vd[axis] += s
        s = get_sign(bc[axis])
        vb[axis] -= s
        vc[axis] += s
        s = get_sign(bd[axis])
        vb[axis] -= s
        vd[axis] += s
        s = get_sign(cd[axis])
        vc[axis] -= s
        vd[axis] += s

    for axis in range(3):
        ab[axis] += va[axis] - vb[axis]
        ac[axis] += va[axis] - vc[axis]
        ad[axis] += va[axis] - vd[axis]
        bc[axis] += vb[axis] - vc[axis]
        bd[axis] += vb[axis] - vd[axis]
        cd[axis] += vc[axis] - vd[axis]

print("DONE!")