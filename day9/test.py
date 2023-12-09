with open('input.txt') as f:
    history_lines = [[int(val) for val in h.strip().split()] for h in f.readlines()]

from collections import Counter


def differences(numbers):
  return [a-b for a,b in zip(numbers[1:], numbers)]


def extrapolate(history):
  diffs = differences(history)
  if len(Counter(diffs)) == 1:
    return history + [history[-1]+diffs[-1]]
  return history + [history[-1]+extrapolate(diffs)[-1]]


print(sum(extrapolate(line)[-1] for line in history_lines))


def extrapolate_backwards(history):
  diffs = differences(history)
  if len(Counter(diffs)) == 1:
    return [history[0]-diffs[0]] + history
  return [history[0]-extrapolate_backwards(diffs)[0]] + history


print(sum(extrapolate_backwards(line)[0] for line in history_lines))