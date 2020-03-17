# -*- coding: utf-8 -*-
""" Agents from the dumb model """

from basicAgents import DiscreteEventAgent
from dumb_model_action_set import DumbActionSet
from dumb_model_action_set_sergio import MyActionSet


class Funny_Bug(DiscreteEventAgent):
    """ A happy Bug"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.dumb_actions_1 = DumbActionSet(self.model, self.spaces['FunnySpace'])
        self.dumb_actions_2 = MyActionSet(self.model, self.spaces['FunnySpace'])

    def step(self, this_step):
        self.my_step = this_step
        self.dumb_actions_2.brazuca_happy_hello(self.my_step)
        self.dumb_actions_1.happy_hello(self.my_step)

       
class Circumspect_Bug(DiscreteEventAgent):
    """ A boring Bug"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.dumb_actions_1 = DumbActionSet(self.model, self.spaces['BoringSpace'])

    def step(self, this_step):
        self.my_step = this_step
        self.dumb_actions_1.formal_hello(self.my_step)
