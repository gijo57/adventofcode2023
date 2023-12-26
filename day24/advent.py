from itertools import combinations

with open('input.txt') as f:
    hailstones = [row.replace(' @ ', '@').split('@') for row in f.read().split('\n')]
    combos = list(combinations(hailstones, 2))
    test_zone = (200000000000000, 400000000000000)
    count = 0

    def is_in_future(intersection, pos_a, velo_a, pos_b, velo_b):
        return (intersection[0] - pos_a[0]) * velo_a[0] >= 0 and (intersection[1] - pos_a[1]) * velo_a[1] >= 0 and (intersection[0] - pos_b[0]) * velo_b[0] >= 0 and (intersection[1] - pos_b[1]) * velo_b[1] >= 0

    for combo in combos:
        try:
            a = combo[0]
            pos_a, velo_a = [int(val.strip()) for val in a[0].split(',')], [int(val.strip()) for val in a[1].split(',')]
            slope_a = velo_a[1] / velo_a[0]
            y_intercept_a = pos_a[1] - pos_a[0] * slope_a

            b = combo[1]
            pos_b, velo_b = [int(val.strip()) for val in b[0].split(',')], [int(val.strip()) for val in b[1].split(',')]
            slope_b = velo_b[1] / velo_b[0]
            y_intercept_b = pos_b[1] - pos_b[0] * slope_b

            x = (y_intercept_a-y_intercept_b)/(slope_b-slope_a)
            y = slope_a * x + y_intercept_a

            intersection = (x, y)
            if (test_zone[0] <= intersection[0] <= test_zone[1] and test_zone[0] <= intersection[1] <= test_zone[1]):
                if (is_in_future(intersection, pos_a, velo_a, pos_b, velo_b)):
                    count += 1
        except ZeroDivisionError:
            continue

    result1 = count
    print(result1)
