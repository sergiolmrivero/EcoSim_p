# -*- coding: utf-8 -*-

"""
Simulation Class (This implements a batch simulation)

"""
import json
from model import Model
from scenarioCreation import ScenarioCreator
from Ecos_p.kernel.get_paths import get_paths

class Simulation(object):
    """This class implements a simulation"""

    def __init__(self, simulation_file):
        """ Initialize the simulation from a json file"""
        with open(simulation_file) as read_file:
            self.json_simulation_defs = json.load(read_file)
        # Get Simulation Paths
        self.simulation_folder = self.json_simulation_defs['simulation_folder']
        print(self.simulation_folder)
        get_paths(self.simulation_folder)
        self.model = Model(self.json_simulation_defs)
        self.initialize_simulation()

    def initialize_simulation(self):
        """ Factory pattern to create a simulation"""
        self.model.simulation = self
        self.name = self.json_simulation_defs["simulation_name"]
        self.simulation_model = self.json_simulation_defs["simulation_model"]
        if self.model.name != self.simulation_model:
            raise Exception(self.model.name,
                            "is not defined in the simulation file")
        for parameter in self.json_simulation_defs['simulation_parameters']:
            self.parameter_name = parameter['parameter_name']
            self.parameter_value = parameter['parameter_value']
            setattr(self, self.parameter_name, self.parameter_value)
        self.model.create_agents()
        self.model.create_observers()
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
