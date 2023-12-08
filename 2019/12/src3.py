import itertools, copy

class Moon:
    def __init__(self, position: int):
        self.position = position
        self.velocity = 0

    def apply_gravity(self, other_moon):
        if self.position < other_moon.position:
            self.velocity += 1
        elif self.position > other_moon.position:
            self.velocity -= 1

    def apply_velocity(self):
        self.position += self.velocity

    def equals(self, other_moon):
        return self.position == other_moon.position and self.velocity == other_moon.velocity


moons = []
with open("input.txt") as file:
    for line in file.readlines():
        parts = line.split('=')
        x = int(parts[1].split(',')[0])
        y = int(parts[2].split(',')[0])
        z = int(parts[3].split('>')[0])
        moons.append(Moon(z))

moons_orig = copy.deepcopy(moons)

for step in range(1000000):
    for moon_a, moon_b in itertools.product(moons, repeat=2):
        if moon_a != moon_b:
            moon_a.apply_gravity(moon_b)

    for moon in moons:
        moon.apply_velocity()

    if moons[0].equals(moons_orig[0]) and \
       moons[1].equals(moons_orig[1]) and \
       moons[2].equals(moons_orig[2]) and \
       moons[3].equals(moons_orig[3]):
        print(step + 1)
        break

print("DONE!")