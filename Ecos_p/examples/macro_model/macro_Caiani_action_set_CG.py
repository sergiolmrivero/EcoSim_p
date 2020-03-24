# -*- coding: utf-8 -*-
"""
Consumer Goods Action Set

"""
# TODO: needs more work

from macro_Caiani_action_set_Goods import GoodsActionSet


class CGActionSet(GoodsActionSet):
    """ Consumers goods action set - Benchmark Model """

    def calculate_labor_demand(self, a_firm):
        """
        A CG Firm calculates the total label demmand for production (NDct)
        This is calculated the using real capital stock for firm (kct) and the
        capital labor ratio for the specific technology (lk).
        NDct = kct/lk
        """
        a_firm.labor_demand = (a_firm.capacity_utilization *
                               (a_firm.capital_stock /
                                a_firm.capital_labor_ratio)
                               )

    def calculate_capacity_utilization(self, a_firm):
        """
        A CG Firm calculates capacity_utilization using capital productivity and
        the firm's capital stock
        """
        a_firm.capacity_utilization = min(1, (a_firm.desired_output_value /
                                              (a_firm.capital_stock *
                                               a_firm.capital_productivity)
                                              )
                                          )
