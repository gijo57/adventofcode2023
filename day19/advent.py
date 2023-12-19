import re

with open('input.txt') as f:
    sections = f.read().split('\n\n')
    workflows = sections[0].split('\n')
    workflows = [x.replace('{', ' ').replace('}', '').split(' ') for x in workflows]
    workflows = {x[0]: x[1] for x in workflows}
    parts = sections[1].split('\n')
    parts = [re.findall('[\d]+', x) for x in parts]
    rating_system = 'xmas'

    def evaluate_rule(rule_value, op, part_value):
        if op == '>':
            return part_value > int(rule_value)
        if op == '<':
            return part_value < int(rule_value)

    def evaluate_part(part, workflow):
        rules, last_rule = workflow.split(',')[:-1], workflow.split(',')[-1]
        for i in range(len(rules)):
            rule = rules[i]
            category, op = rule[0], rule[1]
            value, destination = rule[2:].split(':')
            part_value = int(part[rating_system.index(category)])
            fulfills = evaluate_rule(value, op, part_value)

            if (fulfills and destination == 'A'):
                return True
            elif (fulfills and destination == 'R'):
                return False

            if fulfills:
                return evaluate_part(part, workflows[destination])

            if (i == len(rules) - 1):
                if (last_rule == 'A'):
                    return True
                elif (last_rule == 'R'):
                    return False
                else:
                    return evaluate_part(part, workflows[last_rule])

    total_sum = 0
    starting_workflow = workflows['in']
    for part in parts:
        accepted = evaluate_part(part, starting_workflow)

        if (accepted):
            part_sum = sum([int(x) for x in part])
            total_sum += part_sum

    result1 = total_sum
    print(result1)
