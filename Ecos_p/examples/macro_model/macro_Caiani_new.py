# -*- coding: utf-8 -*-

"""
Model Creation

exec(open('macro_Caiani.py').read())

This method creates reads a yaml file, creates de Simulation object
The simulation object has all classes and specifications to execute de simulation
The agents, schedule, spaces, observers, scenarios, intial values (for the scenarios) are all defined in the yaml file
After the simulation object is created, the simulation is executed (all senarios, and all runs in each scenario)
The results of the scenarios are writen in files in the folder runs
"""
# TODO: Generalize the location specs for the simulation results files (actually in the folder runs)

import importlib

CONFIG_FILE = "Ecos_p_config.json"
ECOS_P_PATH = "/home/rivero/Dropbox/Workspace_Current/Projects/Applications/EcoSim/EcoSim_p/src/v_0-0-2/EcoSim_p/Ecos_p/kernel"

importlib.import_module("Simulation", package="Ecos_p.kernel.simulation")
macro_sim = Simulation(CONFIG_FILE, 'macro_model_config.json', 'macro_Caiani.json')
eco_m = macro_sim.model

macro_sim.execute_simulation()
