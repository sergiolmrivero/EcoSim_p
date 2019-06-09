#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model Creation

*SLMR
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

print(my_sim.agents)
print("")
print("")
print("")
