# -*- coding: utf-8 -*-

"""
Model Creation

This method reads a json file, creates de Simulation object
The simulation object has all classes and specifications to execute de simulation
The agents, schedule, spaces, observers, scenarios, initial values (for the scenarios) are all defined in the yaml file
After the simulation object is created, the simulation is executed (all scenarios, and all runs in each scenario)
The results of the scenarios are writen in files in the folder runs
"""
# TODO: Generalize the location specs for the simulation results files (actually in the folder runs)
import sys
import simulation


def new_simulation(path_to_model, model_config, simulation_defs):
    """ This is the main simulation method without a graphical interface.
        This method receives 3 parameters:
        path_to_model - The path to the model that is executing
        model_config - The configuration file for the model that is executing
        simulation_defs - The model and simulation definition file
    """

    config_file = path_to_model + model_config
    simulation_file = path_to_model + simulation_defs

    new_sim = simulation.Simulation(config_file, simulation_file)

    new_sim.execute_simulation()


if __name__ == "__main__":

    path_to_model = str(sys.argv[1])
    model_config = str(sys.argv[2])
    simulation_defs = str(sys.argv[3])
    new_simulation(path_to_model, model_config, simulation_defs)
