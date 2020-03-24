# -*- coding: utf-8 -*-
"""
Labor Market Action Set
"""

from actions import ActionSet
from agents_accounting import GoodOrService


class LaborActionSet(ActionSet):
    """ Labor Market action set """

    def bid_labor_demand(self):
        """ A firm ask for a quantity of labor at a price """
        pass

    def contract_labor(self, a_firm):
        """ A Firm contracts labor in the labor market at a price """
        offers_available = True
        print(a_firm.my_actions_macro.no_of_offers(a_firm.spaces['Labor_market']))
        while offers_available:
            if a_firm.my_actions_macro.has_offers(a_firm.spaces['Labor_market']):
                a_firm.an_offer = a_firm.my_actions_macro.get_lowest_offer(a_firm.spaces['Labor_market'])
                a_firm.offer_owner = a_firm.an_offer.asset_owner
                a_firm.contracted_labor[a_firm.offer_owner] = a_firm.an_offer
                a_firm.total_contracted_labor += a_firm.an_offer.value
                if a_firm.total_contracted_labor >= a_firm.desired_output_value:
                    a_firm.ready_to_produce = True
                    offers_available = False
                else:
                    offers_available = False
                    print("Labor Market has no offers")

    def pay_salary(self):
        """ Agent pay salaries """
        # TODO: Check if duplicated
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

    def pay_wages(self):
        """ Agent pay wages """
        pass

    def contract_gov_labor(self):
        """ Government get household labor """
        pass
