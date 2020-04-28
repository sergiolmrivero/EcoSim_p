# -*- coding: utf-8 -*-

"""
Definition of the class Model

This class receives a json file with the definition of the simulation scenario and then creates the simulation with all
simulation objects

"""
import random as rnd
import time
from collections import OrderedDict


from agentCreation import AgentPopulationCreator
from observerCreation import ObserverCreator
from scheduleCreation import ScheduleCreator
from spaceCreation import SpaceCreator


class Model:
    """
    Model Basic Class
    Receives the json file name and read it
    Creates all objects in the Simulation
    """

    def __init__(self, json_simulation_defs):
        """Load the definitions of the json file"""
        self.seed = time.time()
        self.random = rnd.Random(self.seed)
        self.simulation = None
        self.json_defs = json_simulation_defs
        self.name = self.json_defs['model_name']
        self.simulation_folder = self.json_defs['simulation_folder']
        self.schedule_def = self.json_defs['schedule']
        self.create_schedule(self.schedule_def)
        self.spaces = dict()
        self.create_spaces()
        self.agents = OrderedDict()
        # self.model_observers = {}
        self.agent_observers = {}

    def create_schedule(self, schedule_def):
        """ Creates the model schedule using the json schedule definition """
        self.schedule_factory = ScheduleCreator(self,
                                                schedule_def)
        self.schedule = self.schedule_factory.provided_schedule

    def create_spaces(self):
        """ Access SpaceFactory (SpaceCreator) and create space objects for the simulation from the json definition """
        self.spaces_def = self.json_defs['spaces']
        self.spaces_factory = SpaceCreator(self, self.spaces_def, self.simulation_folder)
        self.spaces = self.spaces_factory.spaces

    def create_agents(self):
        """
        Access the AgentFactory (AgentPopulationCreator).
        Create the agents
        """
        self.agents_def=self.json_defs['agents']
        self.agents_pop=AgentPopulationCreator(self.simulation, self,
                                               self.agents_def, self.simulation_folder)
        self.agents=self.agents_pop.agents
        self.agents_by_type=self.agents_pop.agents_by_type

    def create_observers(self, path_to_results):
        """
        Access the ObserverFactory (ObserverCreator).
        Create the Observers
        """
        self.agent_observers={}
        self.agent_observers_def=self.json_defs['observers']
        self.agent_observers_pop=ObserverCreator(self, self.simulation,
                                                 self.agent_observers_def, path_to_results)
        self.agent_observers=self.agent_observers_pop.observers

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
