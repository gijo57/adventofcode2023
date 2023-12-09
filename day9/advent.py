with open('input.txt') as f:
    histories = [[int(val) for val in h.strip().split()] for h in f.readlines()]


def get_diffs(values):
    diffs = []
    for i, value in enumerate(values[1:]):
        prev = values[i]
        diff = value - prev
        diffs.append(diff)
    return diffs


def calculate_new_values(diff_lists):
    current_next, current_prev = 0, 0
    for diffs in reversed(diff_lists):
        current_next = diffs[-1] + current_next
        current_prev = diffs[0] - current_prev
    return (current_next, current_prev)


def get_new_values(values, diff_lists):
    diff_lists = diff_lists
    diffs = get_diffs(values)
    diff_lists.append(diffs)
    if (all(v == 0 for v in diffs)):
        next_value, prev_value = calculate_new_values(diff_lists)
        return (next_value, prev_value)
    return get_new_values(diffs, diff_lists)


next_values = []
prev_values = []
for history in histories:
    new_values = get_new_values(history, [history])
    next_values.append(new_values[0])
    prev_values.append(new_values[1])

result1 = sum(next_values)
result2 = sum(prev_values)
print(result1, result2)
