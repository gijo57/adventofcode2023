import numpy as np

with open('input.txt') as f:
    engine_schematic = np.pad(np.array([list(row) for row in f.read().split('\n')]), 1, 'constant', constant_values='.')

    def map_number_positions():
        number_indices = []
        number_to_inspect = []
        indices_to_inspect = []

        for row in range(len(engine_schematic)):
            for index, position in enumerate(engine_schematic[row]):
                if position.isdigit():
                    number_to_inspect.append(position)
                    indices_to_inspect.append(index)
                elif number_to_inspect:
                    number_indices.append([row, ''.join(number_to_inspect), indices_to_inspect])
                    number_to_inspect.clear()
                    indices_to_inspect = []
        return number_indices

    def find_part_numbers(positions):
        part_numbers = []

        for position in positions:
            row_num, number = position[0], int(position[1])
            row = engine_schematic[row_num]
            cols = position[2]
            prev_row = engine_schematic[row_num-1] if row_num-1 >= 0 else []
            next_row = engine_schematic[row_num+1] if row_num+1 < len(engine_schematic) else []
            for col in cols:
                prev_col = int(col)-1 if int(col)-1 >= 0 else col
                next_col = int(col)+1 if int(col)+1 < len(row) else col
                row_neighbors = [row[prev_col], row[next_col]]
                if any(not char.isdigit() and char != '.' for char in row_neighbors):
                    part_numbers.append(number)
                    break
                prev_row_neighbors = [prev_row[prev_col], prev_row[col], prev_row[next_col]]
                if any(not char.isdigit() and char != '.' for char in prev_row_neighbors):
                    part_numbers.append(number)
                    break
                next_row_neighbors = [next_row[prev_col], next_row[col], next_row[next_col]]
                if any(not char.isdigit() and char != '.' for char in next_row_neighbors):
                    part_numbers.append(number)
                    break
        return part_numbers

    def find_gear_ratios(number_positions, engine_schematic):
        ratios = []

        for row_i in range(1, len(engine_schematic)-1):
            for col_i in range(1, len(engine_schematic[row_i])-1):
                if (engine_schematic[row_i][col_i] == '*'):
                    gear_ratio_numbers = []
                    cols_list = [col_i-1, col_i, col_i+1]
                    if ([n for n in number_positions if row_i == n[0]]):
                        numbers = [n for n in number_positions if row_i == n[0]]
                        numbers = [n[1] for n in numbers if set(n[2]).intersection(set(cols_list))]
                        if (numbers):
                            gear_ratio_numbers.extend([int(val) for val in numbers])
                    if ([n for n in number_positions if row_i-1 == n[0]]):
                        numbers = [n for n in number_positions if row_i-1 == n[0]]
                        numbers = [n[1] for n in numbers if set(n[2]).intersection(set(cols_list))]
                        if (numbers):
                            gear_ratio_numbers.extend([int(val) for val in numbers])
                    if ([n for n in number_positions if row_i+1 == n[0]]):
                        numbers = [n for n in number_positions if row_i+1 == n[0]]
                        numbers = [n[1] for n in numbers if set(n[2]).intersection(set(cols_list))]
                        if (numbers):
                            gear_ratio_numbers.extend([int(val) for val in numbers])
                    if len(gear_ratio_numbers) == 2:
                        ratios.append(gear_ratio_numbers[0] * gear_ratio_numbers[1])
        return ratios

    number_positions = map_number_positions()
    part_numbers = find_part_numbers(number_positions)
    gears_ratios = find_gear_ratios(number_positions, engine_schematic)
    result1 = sum(part_numbers)
    result2 = sum(gears_ratios)
    print(result1, result2)
