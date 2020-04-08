# -*- coding: utf-8 -*-
""" This is the Util to Convert a yaml file to a json file """

import yaml
import json

input_file = 'dumb_model_init.yml'
output_file = 'dumb_model_init.json'

with open(input_file, "r") as read_file:
    yaml_defs = yaml.load(read_file, Loader=yaml.FullLoader)
with open(output_file, 'w') as write_file:
    json.dump(yaml_defs, write_file, indent=2)
