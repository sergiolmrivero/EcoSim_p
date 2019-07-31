#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Model Creation

*SLMR


exec(open('fiat_sim.py').read())

"""
from simulation import Simulation

my_sim = Simulation('simulation_init.yaml')
my_model = my_sim.model

my_sim.execute_simulation()

print(my_sim.yaml_simulation_defs)
print("")
print("")
print("")
print(my_model.yaml_defs)

print(my_model.name)
print("")
print("")
print("")

print(my_model.spaces)
print("")
print("")
print("")

print(my_model.agents)
print("")
print("")
print("")
