# -*- coding: utf-8 -*-
"""
Goods Action Set
"""


from actions import ActionSet
from accounting import GoodOrService


class GoodsActionSet(ActionSet):
    """ Dumb model action set """

    def compute_desired_output(self, a_firm, good_type):
        """Agent compute desired output"""

        a_firm.desired_output = GoodOrService(a_firm.name, good_type,
                                              a_firm.desired_output,
                                              a_firm.expected_price,
                                              a_firm)

    def decide_offered_wage(self, a_firm):
        """
        Decide the wage for the quantity of expected
        work that firm wants to contract
        """
        a_firm.offered_wage = a_firm.expected_wage

    def contract_labor(self, a_firm):
        """
        Trabalho total contratado precisa ser ajustado.
        """
        offers_available = True
        print(a_firm.my_actions_labor.no_of_offers(a_firm.spaces['Labor_market']))
        while offers_available:
            if a_firm.actions['has_offers'](a_firm.spaces['Labor_market']):
                a_firm.an_offer = a_firm.actions['get_lowest_offer'](a_firm.spaces['Labor_market'])
                a_firm.offer_owner = a_firm.an_offer.asset_owner
                a_firm.contracted_labor[a_firm.offer_owner] = a_firm.an_offer
                a_firm.total_contracted_labor += a_firm.an_offer.value
                if a_firm.total_contracted_labor >= a_firm.desired_output_value:
                    a_firm.ready_to_produce = True
                    offers_available = False
                else:
                    offers_available = False
                    print("Labor Market has no offers")

    def average_wage(self, a_firm):
        wages = 0
        workers = len(a_firm.contracted_labor)
        if workers > 0:
            for labor_offer in a_firm.contracted_labor.values():
                wages += labor_offer.value
                avg_wage = wages / workers
        else:
            avg_wage = 0
        return avg_wage

    def produce(self, a_firm):
        """ produce """
        pass

    def offer_production(self, a_firm):
        "Agent offer production of consumer goods"
        pass

    def sell_production(self, a_firm):
        "CG_firm sells production"
        pass

    def compute_sales_revenue(self, a_firm):
        "Agent compute sells of CG"
        pass

    def decide_investment(self, a_firm):
        pass

    def contract_credit(self, a_firm):
        pass

    def buy_equipment(self, a_firm):
        pass

    def pay_salaries(self, a_firm):
        pass

    def pay_suppliers(self, a_firm):
        pass

    def pay_interest_bonds(self, a_firm):
        pass

    def pay_interest_loans(self, a_firm):
        pass