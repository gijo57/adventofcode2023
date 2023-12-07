with open('input.txt') as f:
    times, distances = [[int(val) for val in part.split(' ') if val.isdigit()] for part in f.read().split('\n')]
    time_part_2, distance_part_2 = int(''.join([str(val) for val in times])), int(''.join([str(val) for val in distances]))

result1 = 1
for race_num in range(len(times)):
    time = times[race_num]
    record = distances[race_num]
    wins = 0

    for hold in range(time):
        result_distance = hold * (time - hold)
        if result_distance > record:
            wins += 1
    result1 = result1 * wins

result2 = 0
for hold in range(time_part_2):
    result_distance = hold * (time_part_2 - hold)
    if result_distance > distance_part_2:
        result2 += 1

print(result1, result2)
