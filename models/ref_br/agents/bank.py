# -*- coding: utf-8 -*-
""" Banks from the basic macroeconomic model """

from .agents import EconomicAgent


class Bank(EconomicAgent):
    """ A Bank economic agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.credit_market = self.spaces['CreditMarket']
        self.first = True

    def step(self):
        """ Step method for a bank """
        if self.first:
            self.cb = self.get_cb()
            self.gov = self.get_government()
            self.first = False
        # Continue steps

    def get_cb(self):
        """ Get Central Bank from model """
        return self.model.agents_of_type("CentralBank")

    def get_government(self):
        """ Get government from model """
        return self.model.agents_of_type('Government')
