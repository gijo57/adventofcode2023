with open('input.txt') as f:
    parts = f.read().split('\n\n')
    seeds_part_1 = [int(i) for i in parts[0].split(':')[1].split(' ') if i]
    seeds_part_2 = [[i for i in range(seeds_part_1[i:i + 2][0], seeds_part_1[i:i + 2][0] + seeds_part_1[i:i + 2][1])] for i in range(0, len(seeds_part_1), 2)]
    maps = [[[int(val) for val in i.split(' ')] for i in item_map.split(':')[1].split('\n') if i] for item_map in parts[1:]]


def find_locations(seeds):
    lowest_location = float('inf')
    for seed in seeds:
        current_mapped_value = seed
        for item_map in maps:
            for map_row in item_map:
                range_length = map_row[2]
                dest_range_start = map_row[0]
                source_range_start, source_range_end = map_row[1], map_row[1] + range_length - 1
                if source_range_start <= current_mapped_value <= source_range_end:
                    current_mapped_value = dest_range_start + current_mapped_value - source_range_start
                    break
        if (current_mapped_value < lowest_location):
            lowest_location = current_mapped_value
    return lowest_location

result1 = find_locations(seeds_part_1)
result2 = float('inf')
for seeds in seeds_part_2:
    lowest_location = find_locations(seeds)
    if lowest_location < result2:
        result2 = lowest_location
print(result1, result2)

