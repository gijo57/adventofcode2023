with open('example.txt') as f:
    plan = [row.strip().split(' ')[:-1] for row in f.readlines()]

    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    position = [0, 0]

    for instruction in plan[:1]:
        dir = instruction[0]
        dist = int(instruction[1])
        position = [position[0] + (directions[dir][0] * dist), position[1] + (directions[dir][1] * dist)]
