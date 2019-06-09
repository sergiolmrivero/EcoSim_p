#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulation Creation (This implements a batch simulation)

*SLMR
"""
import yaml
from model import Model
from scenario import ScenarioCreator
from agent import AgentPopulationCreator
from observer import ObserverCreator


class Simulation(object):
    """This class implements a simulation"""

    def __init__(self, simulation_file):
        with open(simulation_file, "r") as read_file:
            self.yaml_simulation_defs = yaml.load(read_file)
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
        self.create_scenarios()
        self.create_agents()

    def create_scenarios(self):
        """Scenario creation"""
        self.scenarios_def = self.yaml_simulation_defs['scenarios']
        self.scenarios_factory = ScenarioCreator(self, self.model,
                                                 self.scenarios_def)
        self.scenarios = self.scenarios_factory.scenarios

    def create_agents(self):
        """
        It acess the AgentFactory
        (AgentPopulationCreator).
        Create the agents
        """
        self.agents_def = self.yaml_simulation_defs['agents']
        self.agents_pop = AgentPopulationCreator(self, self.model,
                                                 self.agents_def)
        self.agents = self.agents_pop.agents
        self.agents_by_type = self.agents_pop.agents_by_type

    def create_observers(self):
        """
        It acess the ObserverFactory
        (ObserverCreator).
        Create the Observers
        """
        self.model_observers = {}
        self.agent_observers = {}
        self.model_observers_def = self.yaml_simulation_defs['observers']['model_observers']
        self.agent_observers_def = self.yaml_simulation_defs['observers']['agent_observers']
        self.model_observers = ObserverCreator(self, self.model,
                                                 self.model_observers_def)
        self.model_observers = ObserverCreator(self, self.model,
                                                 self.agent_observers_def)

    def intialize_run(self):
        """Run intialization -
        look at pool design pattern
        Initialize main variables for run
        agents variables and space variables
        """

        pass

    def execute_simulation(self):
        for scenario in self.scenarios.values():
            scenario.execute_scenario()
