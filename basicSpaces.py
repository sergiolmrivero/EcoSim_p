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

    def __init__(self, model, name, actions_set_file,
                 action_class):
        """Initialize Space Class"""
        self.model = model
        self.name = name
        self.actions = dict()
        self.agents = OrderedDict()
        self.create_actions(actions_set_file, action_class)

    def create_actions(self, actions_set_file, action_class):
        self.actions_module = import_module(actions_set_file)
        self.action_set_class_ = getattr(self.actions_module,
                                         action_class)
        self.action_set = self.action_set_class_(self.model,
                                                 self)
        for m in dir(self.action_set):
            if not m.startswith('__'):
                self.actions[m] = getattr(self.action_set, m)

    def enter(self, agent_name, agent):
        if agent_name not in self.agents:
            self.agents[agent_name] = agent

    def exit(self, agent_name):
        if agent_name in self.agents:
            del self.agents[agent_name]

    def action(self, action_name):
        return self.actions[action_name]

    def actions(self):
        return self.actions

    def test_space(self):
        for m in self.actions.keys():
            getattr(self.action_set, m)()