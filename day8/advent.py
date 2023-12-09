with open('input.txt') as f:
    instructions, nodes_list = f.read().split('\n\n')
    nodes_list = nodes_list.split('\n')
    nodes = {}

for node in nodes_list:
    current_node = node[:3]
    nodes[current_node] = (node[7:10], node[12:15])

steps = 0
current_node = 'AAA'
directions = {
    'L': 0,
    'R': 1
}

while current_node != 'ZZZ':
    direction = directions[instructions[steps % len(instructions)]]
    current_node = nodes[current_node][direction]
    steps += 1

print(steps)
