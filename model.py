#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Model

*SLMR
REMEMBER TO USE DEPENDENCE INJECTION IN THE CODE.
http://python-dependency-injector.ets-labs.org/index.html

"""
import yaml
from space import SpaceCreator
from collections import OrderedDict
from agent import AgentPopulationCreator
from observer import ObserverCreator
from schedule import ScheduleCreator


class Model:

    def __init__(self, yaml_file):
        """ Carrega as definicoes do arquivo yaml"""
        self.simulation = None
        self.init_file = yaml_file
        with open(self.init_file, "r") as read_file:
            self.yaml_defs = yaml.load(read_file)
        self.name = self.yaml_defs['model_name']
        self.schedule_def = self.yaml_defs['schedule']
        self.create_schedule(self.schedule_def)
        self.spaces = dict()
        self.create_spaces()
        self.agents = OrderedDict()
        # self.model_observers = {}
        self.agent_observers = {}

    def create_schedule(self, schedule_def):
        self.schedule_factory = ScheduleCreator(self,
                                                schedule_def)
        self.schedule = self.schedule_factory.provided_schedule

    def create_spaces(self):
        """Acessa a SpaceFactory (SpaceCreator) e cria os espaços"""
        self.spaces_def = self.yaml_defs['spaces']
        self.spaces_factory = SpaceCreator(self, self.spaces_def)
        self.spaces = self.spaces_factory.spaces

    def enter_model(self, agent_name, agent):
        if agent_name not in self.agents:
            self.agents[agent_name] = agent

    def exit_model(self, agent_name):
        if agent_name in self.agents:
            del self.agents[agent_name]

    def agents_of_type(self, agent_type):
        return {key: value for key, value in self.agents.items()
                if value.__class__.__name__ == agent_type}

    def agents_by_type(self):
        return OrderedDict({value.__class__.__name__ + "_" + str(key): value
                            for key, value in self.agents.items()})

    def create_agents(self):
        """
        It acess the AgentFactory
        (AgentPopulationCreator).
        Create the agents
        """
        self.agents_def = self.yaml_defs['agents']
        self.agents_pop = AgentPopulationCreator(self.simulation, self,
                                                 self.agents_def)
        self.agents = self.agents_pop.agents
        self.agents_by_type = self.agents_pop.agents_by_type

    def create_observers(self):
        """
        It acess the ObserverFactory
        (ObserverCreator).
        Create the Observers
        """
        self.agent_observers = {}
        self.agent_observers_def = self.yaml_defs['observers']
        self.agent_observers_pop = ObserverCreator(self, self.simulation,
                                                   self.agent_observers_def)
        self.agent_observers = self.agent_observers_pop.observers
