import numpy as np

with open('example.txt') as f:
    contraption = np.pad(np.array([[char+' ' if char != '\\' else char for char in list(row)] for row in f.read().split('\n')]), 1, 'constant', constant_values='V ')

    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    beams = [[1, 1, (0, 1)]]

    def calc_direction(pos, dir):
        char = contraption[pos[0]][pos[1]].strip()
        new_dir = dir
        out_of_bounds = False

        if (char == 'V'):
            out_of_bounds = True
        if (char == '/'):
            if (dir == directions['R']):
                new_dir = directions['U']
            elif (dir == directions['L']):
                new_dir = directions['D']
            elif (dir == directions['D']):
                new_dir = directions['L']
            elif (dir == directions['U']):
                new_dir = directions['R']
        if (char == '\\'):
            if (dir == directions['R']):
                new_dir = directions['D']
            elif (dir == directions['L']):
                new_dir = directions['U']
            elif (dir == directions['D']):
                new_dir = directions['R']
            elif (dir == directions['U']):
                new_dir = directions['L']
        if (char == '|'):
            if (dir == directions['L'] or dir == directions['R']):
                beams.append([pos[0], pos[1], directions['U']])
                new_dir = directions['D']
        if (char == '-'):
            if (dir == directions['U'] or dir == directions['D']):
                beams.append([pos[0], pos[1], directions['L']])
                new_dir = directions['R']
        return new_dir, out_of_bounds

    visited_tiles = set()

    steps = 0
    while beams:
        steps += 1
        beam = beams[0]
        dir = beam[2]
        pos = (beam[0], beam[1])
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        new_dir, out_of_bounds = calc_direction(new_pos, dir)
        visited_tiles.add(new_pos)

        if out_of_bounds:
            beams.pop(0)
        else:
            beams[0][2] = new_dir
            beams[0][0] = new_pos[0]
            beams[0][1] = new_pos[1]

    for tile in visited_tiles:
        if (contraption[tile[0]][tile[1]] != 'V '):
            contraption[tile[0]][tile[1]] = '# '

    print(len(visited_tiles))
