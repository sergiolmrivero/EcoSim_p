# -*- coding: utf-8 -*-
""" Agents from the dumb model """

from basicAgents import DiscreteEventAgent

class Funny_Bug(DiscreteEventAgent):
    """ A happy Bug"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)

    def step(self, this_step):
        self.my_step = this_step
        self.actions['happy_hello'](self.my_step)

class Circumspect_Bug(DiscreteEventAgent):
    """ A boring Bug"""
    def step(self, this_step):
        self.my_step = this_step
        self.actions['formal_hello'](self.my_step)