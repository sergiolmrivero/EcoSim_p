# -*- coding: utf-8 -*-
"""
Labor Market Action Set
"""

from macro_Caiani_action_set import MacroEcoActionSet
from accounting import GoodOrService


class LaborActionSet(MacroEcoActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space

    def compute_desired_output(self):
        "Agent compute desired output"
        pass

    def bid_labor_demand(self):
        "CG_firm ask for a quantity of labor at a price"
        pass

    def contract_labor(self):
        "Agent contract labor in the labor market at a price"
        pass

    def pay_salary(self):
        "Agent Firm pay salaries"
        pass

    def generate_offer(self, hh):
        """ The Household decides wage to offer """
        self.decide_hourly_wage(hh)
        hh.labor_offer = GoodOrService(hh.name, 'w',
                                       hh.labor_capacity,
                                       hh.hourly_wage,
                                       asset_owner_of_gs=hh)

    def decide_hourly_wage(self, hh):
        """ The Household decides wage to offer """
        hh.hourly_wage = hh.expected_wage
