# -*- coding: utf-8 -*-
""" Banks from the basic macroeconomic model """

from .agents import EconomicAgent


class Bank(EconomicAgent):
    """ A Bank economic agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.credit_market = self.spaces['CreditMarket']

    def step(self):
        """ Step method for a bank """
        self.cb = self.get_cb()
        self.gov = self.get_government()
        self.credit_market.decide_cr_target(self)
        self.credit_market.decide_interest_rate_strategy(self)
        self.credit_market.offer_credit(self)
        self.credit_market.calculate_exposure(self)
        self.credit_market.receive_advances_CB(self, self.cb, self.ammount)
        self.credit_market.buy_gov_bonds(self, self.gov, self.ammount)
        self.credit_market.pay_taxes(self)
        self.show_offer()

    def show_offer(self):
        """ A bank show offer """
        print(" I, ", self.name,
              " am working in this model"
              )

    def get_cb(self):
        """ Get Central Bank from model """
        return self.model.agents_of_type('Central_Bank')

    def get_government(self):
        """ Get government from model """
        return self.model.agents_of_type('Government')
