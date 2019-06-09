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
import dependency_injector.providers as providers
import dependency_injector.errors as errors
from importlib import import_module
from schedule import ScheduleCreator


class Space(object):

    def __init__(self, model, name, actions_set_file, action_class, schedule_def):
        """Initialize Space Class"""
        self.model = model
        self.name = name
        self.actions = dict()
        self.agents = dict()
        self.create_schedule(schedule_def)
        self.create_actions(actions_set_file, action_class)

    def create_schedule(self, schedule_def):
        self.schedule_factory = ScheduleCreator(self.model,
                                                self,
                                                schedule_def)
        self.schedule = self.schedule_factory.provided_schedule

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

    def action(self, action_name):
        return self.actions[action_name]

    def actions(self):
        return self.actions

    def test_space(self):
        for m in self.actions.keys():
            getattr(self.action_set, m)()


class SpaceCreator(object):
    """ Space Generator - Space Implemented Subclass must be used"""
    def __init__(self, model, spaces_def):
        self.spaces = dict()
        self.spaces_model = model
        for space_def in spaces_def:
            self.space_type = space_def['space_type']
            self.space_name = space_def['space_name']
            self.space_actions = space_def['action_set']
            self.space_action_class = space_def['action_class']
            self.space_schedule_def = space_def['schedule']
            try:
                self.space_class = eval(self.space_type)
            except NameError:
                print("class ", self.space_type, " is not defined")
            self.space_Factory = SpaceProvider(self.space_class)
            self.space_Factory.add_args(self.spaces_model,
                                        self.space_name,
                                        self.space_actions,
                                        self.space_action_class,
                                        self.space_schedule_def)
            try:
                self.new_space = self.space_Factory()
                self.spaces[self.space_name] = self.new_space
            except errors.Error as exception:
                print(exception)
                # <class '__main__.space_Factory'>
                # does not know <'__main__.self.space_name'>


class SpaceProvider(providers.Factory):
    """ Agent Provider Class"""
    provided_type = Space


# Class examples

class FunnySpace(Space):
    """ A Party"""


class BoringSpace(Space):
    """ A BoringSpace"""
