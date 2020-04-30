# -*- coding: utf-8 -*-
"""
Goods Action Set
"""


from actions import ActionSet
from ..agents_accounting import GoodOrService


class GoodsActionSet(ActionSet):
    """ Goods action set on Macro Benchmark Model"""

    def compute_desired_output(self, a_firm, good_type):
        """
        A firm compute desired output
        The firm computes the inventory percentage that it can maintain
        and the desired output from the expected sales and inventory
        """
        a_firm.desired_perc_inv = a_firm.inventory / a_firm.expected_sales
        a_firm.desired_output_value = (a_firm.expected_sales *
                                       (1 + a_firm.desired_perc_inv) -
                                       a_firm.inventory_t_1)
        a_firm.desired_output = GoodOrService(a_firm.name, good_type,
                                              a_firm.desired_output_value,
                                              a_firm.expected_price,
                                              a_firm)

    def decide_offered_wage(self, a_firm):
        """
        Decide the wage for the quantity of expected
        work that firm wants to contract
        """
        a_firm.offered_wage = a_firm.expected_wage

    def average_wage(self, a_firm):
        """ A firm answers the average wage for contracted labor """
        wages = 0
        workers = len(a_firm.contracted_labor)
        if workers > 0:
            for labor_offer in a_firm.contracted_labor.values():
                wages += labor_offer.value
                avg_wage = wages / workers
        else:
            avg_wage = 0
        return avg_wage

    def offer_production(self, a_firm, ):
        """ Agent offer production of consumer goods """
        pass

    def sell_production(self, a_firm):
        """ CG_firm sells production """
        pass

    def compute_sales_revenue(self, a_firm):
        """ Agent compute sells of CG """
        pass

    def decide_investment(self, a_firm):
        """ A firm decides investment """
        pass

    def contract_credit(self, a_firm):
        """ A firm contracts credit """
        pass

    def buy_equipment(self, a_firm):
        """ A firm buys production equipment (fixed capital) """
        pass

    def pay_salaries(self, a_firm):
        """ A firm pays salaries """
        pass

    def pay_suppliers(self, a_firm):
        """ A firm pays suppliers of goods """
        pass

    def pay_interest_bonds(self, a_firm):
        """ A firm pays interest on bonds to investors """
        pass

    def pay_interest_loans(self, a_firm):
        """A firm pays interest on loans to a bank"""
        pass
