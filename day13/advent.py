import numpy as np

with open('example.txt') as f:
    patterns = [np.array([list(row) for row in pattern.split('\n')]) for pattern in f.read().split('\n\n')]
    pattern_length = len(patterns[0])

def find_reflection_point(pattern):
        for i, row in enumerate(pattern[1:]):
            if (str(row) == str(pattern[i])):
                return i + 1

def get_full_reflection(pattern, point):
    part1 = [''.join(row) for row in pattern[:point]]
    part2 = [''.join(row) for row in pattern[point:]]
    first = part1 if len(part1) <= len(part2) else part2
    second = part1 if len(part1) >= len(part2) else part2
    second = list(reversed(second))

    for i, row in enumerate(first):
        row2 = second[i]
        if (row != row2):
            pass



for pattern in patterns:
    print('----')
    rotated_pattern = np.rot90(pattern, axes=(1, 0))
    horizontal_reflection_point = find_reflection_point(pattern)
    vertical_reflection_point = find_reflection_point(rotated_pattern)

    horizontal_reflection = get_full_reflection(pattern, horizontal_reflection_point)
    vertical_reflection = get_full_reflection(rotated_pattern, vertical_reflection_point)

