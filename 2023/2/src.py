def get_power(sets):
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for s in sets:
        for cubes in s:
            cubes = cubes.split(" ")
            number, color = int(cubes[0]), cubes[1]
            min_cubes[color] = max(min_cubes[color], number)
    power = 1
    for number in min_cubes.values():
        power *= number
    return power


power_sum = 0
with open("input.txt") as file:
    for line in file.readlines():
        game, sets = line.strip().split(": ")
        game_id = int(game.split(" ")[1])
        sets = sets.split("; ")
        sets = [s.split(", ") for s in sets]
        power = get_power(sets)
        power_sum += power

print(power_sum)
