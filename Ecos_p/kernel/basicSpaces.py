#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The space class and the associated classes
*SLMR

inspired by:
http://code.activestate.com/recipes/131499-observer-pattern/

*TL;DR80
Maintains a list of dependents and notifies them of any state changes.


"""
from importlib import import_module
from collections import OrderedDict


class Space(object):

    def __init__(self, model, name,
                 actions_set_file,
                 action_class):
        """Initialize Space Class"""
        self.model = model
        self.name = name
        self.agents = OrderedDict()

    def enter(self, agent_name, agent):
        if agent_name not in self.agents:
            self.agents[agent_name] = agent

    def exit(self, agent_name):
        if agent_name in self.agents:
            del self.agents[agent_name]
