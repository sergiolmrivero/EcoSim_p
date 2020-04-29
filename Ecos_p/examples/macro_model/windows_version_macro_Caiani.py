

"""
Model Creation

exec(open('macro_Caiani.py').read())

This method creates reads a yaml file, creates de Simulation object
The simulation object has all classes and specifications to execute de simulation
The agents, schedule, spaces, observers, scenarios, initial values (for the scenarios) are all defined in the yaml file
After the simulation object is created, the simulation is executed (all scenarios, and all runs in each scenario)
The results of the scenarios are writen in files in the folder runs
"""
# TODO: Generalize the location specs for the simulation results files (actually in the folder runs)
import sys
import importlib

PATH_TO_MODEL = 'C:\Users\Sergio Rivero\Documents\GitHub\EcoSim_p-versao-0.0.2\Ecos_p\examples\macro_model'
PATH_TO_KERNEL = 'C:\Users\Sergio Rivero\Documents\GitHub\EcoSim_p-versao-0.0.2\Ecos_p\kernel'

sys.path.insert(0, PATH_TO_KERNEL)

import simulation as sim

model_config = PATH_TO_MODEL + '\macro_model_config.json'
model_defs = PATH_TO_MODEL + '\macro_Caiani.json'
macro_sim = sim.Simulation(model_config, model_defs)

macro_sim.execute_simulation()
