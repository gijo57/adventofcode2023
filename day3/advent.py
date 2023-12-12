import numpy as np

with open('example.txt') as f:
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
                    number_indices.append([str(row)+'-'+''.join(number_to_inspect), indices_to_inspect])
                    number_to_inspect.clear()
                    indices_to_inspect = []
        return number_indices


    def find_part_numbers(positions):
        part_numbers = []
        gear_numbers = []

        for key, cols in positions:
            row_num, number = [int(val) for val in key.split('-')]
            row = engine_schematic[row_num]
            prev_row = engine_schematic[row_num-1] if row_num-1 >= 0 else []
            next_row = engine_schematic[row_num+1] if row_num+1 < len(engine_schematic) else []

            for col in cols:
                prev_col = int(col)-1 if int(col)-1 >= 0 else col
                next_col = int(col)+1 if int(col)+1 < len(row) else col
                row_neighbors = [row[prev_col], row[next_col]]
                if any(not char.isdigit() and char != '.' for char in row_neighbors):
                    part_numbers.append(number)
                    if any(char == '*' for char in row_neighbors):
                        gear_numbers.append(number)
                    break
                prev_row_neighbors = [prev_row[prev_col], prev_row[col], prev_row[next_col]]
                if any(not char.isdigit() and char != '.' for char in prev_row_neighbors):
                        part_numbers.append(number)
                        if any(char == '*' for char in prev_row_neighbors):
                            gear_numbers.append(number)
                        break
                next_row_neighbors = [next_row[prev_col], next_row[col], next_row[next_col]]
                if any(not char.isdigit() and char != '.' for char in next_row_neighbors):
                        part_numbers.append(number)
                        if any(char == '*' for char in next_row_neighbors):
                            gear_numbers.append(number)
                        break
        print(gear_numbers)
        return part_numbers


    number_positions = map_number_positions()
    part_numbers = find_part_numbers(number_positions)
    result1 = sum(part_numbers)
    print(result1)
