# -*- coding: utf-8 -*-

"""
Simulation Class (This implements a batch simulation)

"""
import yaml
from model import Model
from scenarioCreation import ScenarioCreator


class Simulation(object):
    """This class implements a simulation"""

    def __init__(self, simulation_file):
        """ Initialize the simulation from a yaml file"""
        with open(simulation_file, "r") as read_file:
            self.yaml_simulation_defs = yaml.load(read_file, Loader=yaml.FullLoader)
        self.model = Model(simulation_file)
        self.initialize_simulation()

    def initialize_simulation(self):
        """ Factory pattern to create a simulation"""
        self.model.simulation = self
        self.name = self.yaml_simulation_defs["simulation_name"]
        self.simulation_model = self.yaml_simulation_defs["simulation_model"]
        if self.model.name != self.simulation_model:
            raise Exception(self.model.name,
                            "is not defined in the simulation file")
        for parameter in self.yaml_simulation_defs['simulation_parameters']:
            self.parameter_name = parameter['parameter_name']
            self.parameter_value = parameter['parameter_value']
            setattr(self, self.parameter_name, self.parameter_value)
        self.model.create_agents()
        self.model.create_observers()
        self.create_scenarios()

    def create_scenarios(self):
        """ Scenario creation """
        self.scenarios_def = self.yaml_simulation_defs['scenarios']
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

        This method gets all scenarios in the yaml definition and executes
        the defined number of runs for each scenario
        """
        for scenario in self.scenarios.values():
            scenario.execute_scenario()
