import re

with open('input.txt') as f:
    sequence = f.readlines()[0].split(',')

    def calc_value(string):
        current_value = 0
        for char in string:
            current_value += ord(char)
            current_value *= 17
            current_value = current_value % 256
        return current_value

    string_values = []
    for string in sequence:
        current_value = calc_value(string)
        string_values.append(current_value)

    result1 = sum(string_values)

    boxes = {}
    labels_in_boxes = {}
    for string in sequence:
        focal_length = ''
        parts = re.findall(r'[a-z]+|[=|-]|[0-9]+', string)
        label, op = parts[0], parts[1]

        if (len(parts) == 3):
            focal_length = parts[2]

        box_has_lens = False
        box_no = calc_value(label)
        lens = (label, op, focal_length)
        if (box_no in boxes):
            box_has_lens = len([lens for lens in boxes[box_no] if label in lens]) > 0

        if (op == '-'):
            if (box_has_lens):
                lens_to_remove = [lens for lens in boxes[box_no] if label in lens][0]
                boxes[box_no].remove(lens_to_remove)
        else:
            if (box_no not in boxes):
                boxes[box_no] = [lens]
            else:
                if (not box_has_lens):
                    boxes[box_no].append(lens)
                else:
                    lens_index = boxes[box_no].index([lens for lens in boxes[box_no] if label in lens][0])
                    boxes[box_no][lens_index] = lens

    focusing_powers = []

    for box_no, lenses in boxes.items():
        focusing_power = 0
        for i, lens in enumerate(lenses):
            individual_focusing_power = int(box_no + 1) * (i + 1) * int(lens[-1])
            focusing_powers.append(individual_focusing_power)

    result2 = sum(focusing_powers)
    print(result1, result2)