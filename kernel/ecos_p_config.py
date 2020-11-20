import json
import os
import sys


def get_paths(print_results=False, config_file="config.json"):

    with open(config_file) as read_file:
        json_simulation_defs = json.load(read_file)
    paths_dict = json_simulation_defs['Paths']
    for path_name, path_value in paths_dict.items():
        if os.path.isdir(path_value):
            sys.path.append(path_value)
        else:
            message = 'the folder ' + path_name + ' does not exist \n path address : ' + path_value
            raise Exception(message)

    if print_results:
        print('\nDIRECTORIES')
        for key, value in paths_dict.items():
            print(key, ': ', value)

    return paths_dict