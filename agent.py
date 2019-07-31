#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Agent

*SLMR
REMEMBER TO USE DEPENDENCE INJECTION IN THE CODE.
http://python-dependency-injector.ets-labs.org/index.html

"""
import dependency_injector.providers as providers
import dependency_injector.errors as errors
from event import Event


class Agent(object):

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Agent Initialization
            Incorporar as variaveis de agente na implementação"""
        self.name = agent_def['agent_prefix'] + '_' + str(agent_number)
        self.simulation = simulation
        self.model = model
        self.spaces = dict()
        self.alive = False
        self.model.enter_model(self, self.name)
        self.agent_actions = agent_def['agent_actions']
        self.actions = dict()
        for space_name in agent_def['agent_spaces']:
            try:
                self.enter_space(space_name)
                self.get_my_actions(self.spaces[space_name])
            except KeyError:
                print("There is no space called ", space_name,
                      " in this model")

    def enter_space(self, space_name):
        """ Agent enter space """
        self.model.spaces[space_name]
        self.spaces[space_name] = self.model.spaces[space_name]
        self.spaces[space_name].enter(self.name, self)

    def get_action(self, space, action_name):
        self.actions[action_name] = space.action(action_name)

    def get_all_actions(self, space):
        self.actions = space.actions

    def get_my_actions(self, space):
        for action_name in self.agent_actions:
            try:
                self.actions[action_name] = space.actions[action_name]
            except KeyError:
                print("There is no action called ", action_name,
                      " in the space called", space.name)

    def get_atrribute(self, attribute_name):
        try:
            this_attribute = None
            this_attribute = self.__getattribute__(attribute_name)
        except AttributeError:
            print("There is no attribute called ", attribute_name,
                  " in agent ", self.name)
        else:
            return this_attribute

    def alive(self):
        """ Agent set to alive """
        self.alive = True

    def dead(self):
        """ Agent set to dead """
        self.alive = False

    def executionLoop(self):
        """ An Agent execution loop """
        while self.alive:
            self.step()

    def step(self):
        """ Agent standard step - can be specialized by subclass """


class DiscreteEventAgent(Agent):

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Agent Initialization
            Incorporar as variaveis de agente na implementação"""
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_step = 0

    def step(self, this_step):
        """ Agent standard step - can be specialized by subclass ]
            -- The code below is only an example
        """
        self.my_step = this_step
        for action in self.actions.values():
            action(self.my_step)


class EventAgent(Agent):

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Agent Initialization
            Incorporar as variaveis de agente na implementação"""
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_step = 0

    def step(self, this_step):
        """ Agent standard step - can be specialized by subclass ]
            -- The code below is only an example
        """
        self.my_step = this_step
        for a_space in self.spaces.values():
            for action in a_space.actions.values():
                self.an_event = Event(self, self, action)
                self.an_event.set_status('active')
                a_space.schedule.collect_event(self.an_event)

        #  action(self.my_step)


class AgentPopulationCreator(object):
    """
    Agent Population Generator
    Agent Implemented Subclass must be used
    """
    def __init__(self, simulation, model, agents_def):
        self.agents = dict()
        self.agents_by_type = dict()
        self.agents_simulation = simulation
        self.agents_model = model
        for agent_def in agents_def:
            self.agent_type = agent_def['agent_type']
            self.agent_prefix = agent_def['agent_prefix']
            self.agent_population_size = int(agent_def['no_of_agents'])
            try:
                self.agent_class = eval(self.agent_type)
                self.agents_by_type[self.agent_type] = dict()
            except NameError:
                print("class ", self.agent_type, " is not defined")
            for agent_number in range(self.agent_population_size):
                self.agent_Factory = AgentProvider(self.agent_class)
                self.agent_name = self.agent_prefix + '_' + str(agent_number)
                self.agent_Factory.add_args(self.agents_simulation,
                                            self.agents_model,
                                            agent_number,
                                            agent_def)
                try:
                    self.new_agent = self.agent_Factory()
                    self.agents[self.agent_name] = self.new_agent
                    self.agents_by_type[self.agent_type][self.agent_name] = self.new_agent
                except errors.Error as exception:
                    print(exception)
                    # <class '__main__.agent_Factory'>
                    # does not know <'__main__.self.agent_name'>

    # def set_memory(self, a_memory=None):
    #     if a_memory is None:
    #         self.memory = Memory(self)
    #     else:
    #         self.memory = a_memory

    # def set_decision_mechanism(self, a_decision_mechanism=None):
    #     if a_decision_mechanism is None:
    #         self.decision_mechanism = Decision_Mechanism(self)
    #     else:
    #         self.decision_mechanism = a_decision_mechanism

    # def update_event(self, event):
    #     """ Update agent memory """
    #     self.memory.update_event(event)

    # def acts(self, an_event):
    #     # Precisa reduzir o acoplamento aqui
    #     an_event.set_status('active')
    #     self.spaces[an_event.space_name].collect_event(an_event)

    # def create_event(self, an_action):
    #     return Event(self, self.a_space, an_action)


class AgentProvider(providers.Factory):
    """ Agent Provider Class"""
    provided_type = Agent


# Class examples

class Funny_Bug(DiscreteEventAgent):
    """ A Bug"""


class Circumspect_Bug(DiscreteEventAgent):
    """ A Bug"""
