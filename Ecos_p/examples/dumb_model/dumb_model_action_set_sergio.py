# -*- coding: utf-8 -*-
"""
Dumb Model Action Set
"""

from actions import ActionSet


class MyActionSet(ActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space

    def brazuca_happy_hello(self, step):
        print("E aí, moçada????")
        print("Step: ", step)
        self.sim_info()

    def formal_hello(self, step):
        print("Hello, Sir World. I am very glad to meet you.")
        print("Step: ", step)
        self.sim_info()

    def simple_hello(self, step):
        print("Hello, World.")
        print("Step: ", step)
        self.sim_info()

    def sim_info(self):
        print("")
        print("Model: ", self.model.name)
        self.scenario_name = self.model.schedule.scenario_name
        self.this_run = self.model.schedule.run_nr
        print("Scenario: ", self.scenario_name)
        print("Run: ", self.this_run)
        print("------------")
