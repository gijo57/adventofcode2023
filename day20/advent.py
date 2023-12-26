with open('example1.txt') as f:
    configurations = [[x.strip() for x in conf.split('->')] for conf in f.read().split('\n')]

    config_states = {

    }

    def get_config_info(config):
        type = config[0][0]
        name = config[0][1:]
        destinations = [x.strip() for x in config[1].split(',')]

        if (config[0] == 'broadcaster'):
            type = None
            name = config[0]

        return type, name, destinations

    rounds = 0
    while rounds < 3:
        for config in configurations:
            type, name, destinations = get_config_info(config)
            print(type, name, destinations)
            rounds += 1
