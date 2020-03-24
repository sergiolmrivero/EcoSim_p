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

import sys
#import yappi

sys.path.insert(0, '../../kernel')

from simulation import Simulation

macro_sim = Simulation('macro_Caiani.yml')
eco_m = macro_sim.model
#yappi.start()
macro_sim.execute_simulation()

#yappi.get_func_stats().print_all()
#yappi.get_thread_stats().print_all(
