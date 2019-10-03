# -*- coding: utf-8 -*-
""" Agents from the dumb model """

import agent
from agent import DiscreteEventAgent

class Funny_Bug(DiscreteEventAgent):
    """ A happy Bug"""
    def step(self, this_step):
        self.my_step = this_step
        self.actions['happy_hello'](self.my_step)
        self.actions['happy_hello'](self.my_step)


class Circumspect_Bug(DiscreteEventAgent):
    """ A boring Bug"""
    def step(self, this_step):
        self.my_step = this_step
        self.actions['formal_hello'](self.my_step)
