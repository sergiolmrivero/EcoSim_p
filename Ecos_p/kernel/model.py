# -*- coding: utf-8 -*-

"""
Definition of the class Model

This class receives a yaml file with the definition of the simulation scenario and then creates the simulation with all
simulation objects

"""
import yaml
import random as rnd
import time
from collections import OrderedDict
from spaceCreation import SpaceCreator
from agentCreation import AgentPopulationCreator
from scheduleCreation import ScheduleCreator
from observerCreation import ObserverCreator


class Model:
    """
    Model Basic Class
    Receives the yaml file name and read it
    Creates all objects in the Simulation
    """

    def __init__(self, yaml_file):
        """Load the definitions of the yaml file"""
        self.seed = time.time()
        self.random = rnd.Random(self.seed)
        self.simulation = None
        self.init_file = yaml_file
        with open(self.init_file, "r") as read_file:
            self.yaml_defs = yaml.load(read_file, Loader=yaml.FullLoader)
        self.name = self.yaml_defs['model_name']
        self.schedule_def = self.yaml_defs['schedule']
        self.create_schedule(self.schedule_def)
        self.spaces = dict()
        self.create_spaces()
        self.agents = OrderedDict()
        # self.model_observers = {}
        self.agent_observers = {}

    def create_schedule(self, schedule_def):
        """ Creates the model schedule using the yaml schedule definition """
        self.schedule_factory = ScheduleCreator(self,
                                                schedule_def)
        self.schedule = self.schedule_factory.provided_schedule

    def create_spaces(self):
        """ Access SpaceFactory (SpaceCreator) and create space objects for the simulation from the yaml definition """
        self.spaces_def = self.yaml_defs['spaces']
        self.spaces_factory = SpaceCreator(self, self.spaces_def)
        self.spaces = self.spaces_factory.spaces

    def enter_model(self, agent_name, agent):
        """ An agent enters the model (is included in agents dict) """
        if agent_name not in self.agents:
            self.agents[agent_name] = agent

    def exit_model(self, agent_name):
        """ An agent exits the model (is deleted from agents dict) """
        if agent_name in self.agents:
            del self.agents[agent_name]

    def agents_of_type(self, agent_type):
        """ Returns a dict with the agents with an specific type """
        # TODO: Check this method
        return {key: value for key, value in self.agents.items()
                if value.type == agent_type}

    def agents_by_type(self):
        """ Returns a dict with all agents in the simulation  ordered by type (agent specific class) """
        return OrderedDict({value.__class__.__name__ + "_" + str(key): value
                            for key, value in self.agents.items()})

    def agents_number(self):
        """ Returns how many agents we have in the simulation (size of agents dict) """
        return len(self.agents)

    def agents_of_type_number(self, agent_type):
        """ Returns how many agents of an specific type """
        return len({key: value for key, value in self.agents.items()
                    if value.__class__.__name__ == agent_type})

    def mixed_agents(self):
        """ Returns a randomly shuffled list of agents (from agents dict) """
        agents_names = list(self.agents.keys())
        self.random.shuffle(agents_names)

        for agent_name in agents_names:
            if agent_name in self.agents:
                yield self.agents[agent_name]

    def create_agents(self):
        """
        Access the AgentFactory (AgentPopulationCreator).
        Create the agents
        """
        self.agents_def = self.yaml_defs['agents']
        self.agents_pop = AgentPopulationCreator(self.simulation, self,
                                                 self.agents_def)
        self.agents = self.agents_pop.agents
        self.agents_by_type = self.agents_pop.agents_by_type

    def create_observers(self):
        """
        Access the ObserverFactory (ObserverCreator).
        Create the Observers
        """
        self.agent_observers = {}
        self.agent_observers_def = self.yaml_defs['observers']
        self.agent_observers_pop = ObserverCreator(self, self.simulation,
                                                   self.agent_observers_def)
        self.agent_observers = self.agent_observers_pop.observers