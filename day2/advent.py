import math

with open('input.txt') as f:
    games = f.read().split('\n')
    limits = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

result1, result2 = 0, 0
powers_of_sets = []

for game in games:
    least_cubes = {}
    is_valid = True
    id = int(game.split(':')[0].split(' ')[1])
    subsets = game[game.find(':')+1:].split(';')

    for subset in subsets:
        colors = [color.strip().split(' ') for color in subset.split(',')]

        for color in colors:
            name, value = color[1], int(color[0])
            limit = limits[name]

            if name not in least_cubes or value > least_cubes[name]:
                least_cubes[name] = value

            if (value > limit):
                is_valid = False

    powers_of_sets.append(math.prod([i for i in least_cubes.values()]))
    if is_valid:
        result1 += id

result2 = sum(powers_of_sets)

print(result1, result2)
