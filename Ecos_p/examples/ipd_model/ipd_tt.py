# -*- coding: utf-8 -*-

"""
Model Creation

exec(open('ipd.py').read())

This method creates reads a yaml file, creates de Simulation object
The simulation object has all classes and specifications to execute de simulation
The agents, schedule, spaces, observers, scenarios, initial values (for the scenarios) are all defined in the yaml file
After the simulation object is created, the simulation is executed (all scenarios, and all runs in each scenario)
The results of the scenarios are writen in files in the folder runs
"""
# TODO: Generalize the location specs for the simulation results files (actually in the folder runs)
import sys
import importlib

PATH_TO_MODEL = '/home/rivero/Dropbox/Workspace_Current/Projects/Applications/EcoSim/EcoSim_p/src/EcoSim_p/Ecos_p/examples/ipd_model/'
PATH_TO_KERNEL = '/home/rivero/Dropbox/Workspace_Current/Projects/Applications/EcoSim/EcoSim_p/src/EcoSim_p/Ecos_p/kernel/'

sys.path.insert(0, PATH_TO_KERNEL)

import simulation as sim
model_config = PATH_TO_MODEL + 'ipd_model_config.json'
model_defs = PATH_TO_MODEL + 'ipd_tt.json'
ipd_sim = sim.Simulation(model_config, model_defs )

ipd_sim.execute_simulation()
