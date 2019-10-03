#!/usr/bin/env python
# -*- coding: utf-8 -*-


from actions import ActionSet


class DumbActionSet(ActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space

    def happy_hello(self, step):
        return(print("Hello!! Wonderfull World!!!!"))
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
