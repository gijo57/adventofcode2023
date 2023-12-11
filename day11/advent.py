from itertools import combinations
import numpy as np

with open('input.txt') as f:
    image = np.array([list(row.strip()) for row in f.readlines()])
    galaxies = [[x, y] for x in range(len(image[0])) for y in range(len(image)) if image[x][y] == '#']
    empty_rows = [i for i in range(len(image)) if all(val == '.' for val in image[i])]
    empty_cols = [i for i in range(len(image[0])) if all(val == '.' for val in image[:, i])]

expanded_galaxies = []
super_expanded_galaxies = []
for galaxy in galaxies:
    added_rows = sum(galaxy[0] > row for row in empty_rows)
    added_cols = sum(galaxy[1] > col for col in empty_cols)
    expanded_galaxy = [galaxy[0] + added_rows, galaxy[1] + added_cols]
    expanded_galaxies.append(expanded_galaxy)
    super_expanded_galaxy = [galaxy[0] + added_rows * 999999, galaxy[1] + added_cols * 999999]
    super_expanded_galaxies.append(super_expanded_galaxy)

expanded_pairs = combinations(expanded_galaxies, 2)
super_expanded_pairs = combinations(super_expanded_galaxies, 2)

expanded_dist_sum = 0
for pair in expanded_pairs:
    galaxy1, galaxy2 = pair[0], pair[1]
    dist = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    expanded_dist_sum += dist

super_expanded_dist_sum = 0
for pair in super_expanded_pairs:
    galaxy1, galaxy2 = pair[0], pair[1]
    dist = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    super_expanded_dist_sum += dist

result1, result2 = expanded_dist_sum, super_expanded_dist_sum
print(result1, result2)
