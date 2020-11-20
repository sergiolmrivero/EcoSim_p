# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from .agents import EconomicAgent


class Government(EconomicAgent):
    """ The Government economic agetn """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.labor_market = self.spaces['LaborMarket']
        self.credit_market = self.spaces['CreditMarket']
        self.deposits_market = self.spaces['DepositsMarket']

    def step(self, this_step):
        """ Step method for Government Agent """
        self.my_step = this_step
        self.calculate_available_resources()
        self.labor_market.contract_gov_labor()
        self.deposits_market.pay_unempl_benefits()
        self.labor_market.pay_wages()
        self.credit_market.pay_gov_bonds_interest()
        self.credit_market.offer_new_bonds()
        self.show_offer()

    def show_offer(self):
        """ Government show offer"""
        print(" I, ", self.name,
              " am working in this model  BCBCBCBBCBCBCBCBCBCBCBCBCBC"
              )

    def calculate_available_resources(self):
        """ Government Calculates Available resources"""
        pass
