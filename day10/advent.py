import numpy as np

with open('input.txt') as f:
    pipe_map = np.pad(np.array([list(row.strip()) for row in f.readlines()]), 1, 'constant', constant_values='.')
    steps = 1

    possible_neighbors = {
        (-1, 0): ['|', '7', 'F'],  # UP
        (1, 0): ['|', 'J', 'L'],  # DOWN
        (0, -1): ['-', 'L', 'F'],  # LEFT
        (0, 1): ['-', 'J', '7']  # RIGHT
    }

    possible_dirs = {
        '|': [(-1, 0), (1, 0)],
        '-': [(0, -1), (0, 1)],
        'L': [(-1, 0), (0, 1)],
        'J': [(0, -1), (-1, 0)],
        '7': [(0, -1), (1, 0)],
        'F': [(1, 0), (0, 1)],
        '.': []
    }

    def find_next_pos(tile, prev_pos, curr_pos):
        neighbors = []

        for coords in possible_neighbors.keys():
            neighbor_coords = (curr_pos[0] + coords[0], curr_pos[1] + coords[1])
            neighbor = pipe_map[neighbor_coords]
            if neighbor in possible_neighbors[coords]:
                if tile == 'S':
                    neighbors.append(neighbor_coords)
                else:
                    if prev_pos != neighbor_coords:
                        if coords in possible_dirs[tile]:
                            return (neighbor_coords, curr_pos)

        return neighbors if tile == 'S' else 0

    start_pos = np.where(pipe_map == 'S')
    reverse_pos, pos = find_next_pos('S', start_pos, start_pos)
    reverse_prev_pos, prev_pos = start_pos, start_pos

    while reverse_pos != pos:
        reverse_tile = pipe_map[reverse_pos[0], reverse_pos[1]][0]
        tile = pipe_map[pos[0], pos[1]][0]
        reverse_pos, reverse_prev_pos = find_next_pos(reverse_tile, reverse_prev_pos, reverse_pos)
        pos, prev_pos = find_next_pos(tile, prev_pos, pos)
        steps += 1

result1 = steps
print(result1)
