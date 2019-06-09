#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from actions import ActionSet


class DumbActionSet(ActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space

    def happy_hello(self, step):
        print("Hello!! Wonderfull World!!!!")
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
        self.scenario_name = self.space.schedule.scenario_name
        self.this_run = self.space.schedule.run_nr
        print("Scenario: ", self.scenario_name)
        print("Run: ", self.this_run)
        print("------------")
