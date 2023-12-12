with open('example.txt') as f:
    rows = [[[int(val) if val.isdigit() else val for val in x.split(',')] for x in row.strip().split(' ')] for row in f.readlines()]
    print(rows[0])