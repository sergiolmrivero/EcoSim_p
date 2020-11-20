# -*- coding: utf-8 -*-

"""
Simulation Class (This implements a batch simulation)

"""
import json
import sys
from model import Model
from scenarioCreation import ScenarioCreator


class Simulation(object):
    """This class implements a simulation"""

    def __init__(self, simulation_config_file, simulation_file):
        """ Initialize a Simulation """

        # Read the simulation configuration file
        with open(simulation_config_file) as read_file:
            self.simulation_config = json.load(read_file)

        # Initialize the simulation from a json file
        with open(simulation_file) as read_file:
            self.json_simulation_defs = json.load(read_file)

        # Get Simulation Paths
        self.path_to_model = self.simulation_config['paths']['model']
        self.path_to_results = self.simulation_config['paths']['results']
        sys.path.insert(0, self.path_to_model)
        self.initialize_simulation()

    def initialize_simulation(self):
        """ Factory pattern to create a simulation"""
        self.name = self.json_simulation_defs["simulation_name"]

        self.model = Model(self, self.json_simulation_defs, self.path_to_results)

        for parameter in self.json_simulation_defs['simulation_parameters']:
            self.parameter_name = parameter['parameter_name']
            self.parameter_value = parameter['parameter_value']
            setattr(self, self.parameter_name, self.parameter_value)
        self.create_scenarios()

    def create_scenarios(self):
        """ Scenario creation """
        self.scenarios_def = self.json_simulation_defs['scenarios']
        self.scenarios_factory = ScenarioCreator(self, self.model,
                                                 self.scenarios_def)
        self.scenarios = self.scenarios_factory.scenarios

    def intialize_run(self):
        """
        Run initialization -
        Initialize main variables for run
        agents variables and space variables
        """
        # TODO: Look at pool design pattern to reduce simulation creation overload
        # TODO: To Be Defined
        pass

    def execute_simulation(self):
        """
        Executes a Simulation.

        This method gets all scenarios in the json definition and executes
        the defined number of runs for each scenario
        """
        for scenario in self.scenarios.values():
            scenario.execute_scenario()
