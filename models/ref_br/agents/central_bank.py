# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from .agents import EconomicAgent


class CentralBank(EconomicAgent):
    """ The Central Bank economic agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.credit_market = self.spaces['CreditMarket']
        #self.deposits_market = self.spaces['DepositsMarket']

    def step(self):
        """ Step method for the Central bank Agent """
        self.decide_monetary_policy()

    def decide_monetary_policy(self):
        """Central Bank decides monetary policy"""
        pass

    def get_government(self):
        """ Get government from model """
        return self.model.agents_of_type('Government')
