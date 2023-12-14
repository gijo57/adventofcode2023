import numpy as np
import re
import itertools
import timeit
start_time = timeit.default_timer()

with open('input.txt') as f:
    platform = np.array([list(row.strip()) for row in f.readlines()])
    rotated_platform = np.rot90(platform)
    row_len = len(rotated_platform[0])
    delimiter = '#'
    total_load = 0

    for row in range(len(rotated_platform)):
        split_row = [sorted(part, reverse=True) if '#' not in part else part for part in re.split('(#)', ''.join(rotated_platform[row])) if part]
        new_row = np.array(list(itertools.chain.from_iterable(split_row)))
        row_load = sum([row_len - i for i in np.where(new_row == 'O')[0]])
        total_load += row_load

    result1 = total_load
    print(result1)

elapsed = timeit.default_timer() - start_time
print((elapsed * 1000000000) / 60 / 60 / 24)