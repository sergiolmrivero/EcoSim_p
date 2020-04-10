# -*- coding: utf-8 -*-
"""
Capital Goods Market Action Set

"""

from macro_Caiani_action_set_Goods import GoodsActionSet


class KGActionSet(GoodsActionSet):
    """ Capital Goods Action Set """

    def calculate_labor_demand(self, a_firm):
        """
        A KG Firm calculates the total label demmand for production (NDct)
        This is calculated the using desired output (yD_kt) and the
        labor productivity (mi_N)
        NDct = yD_kt/mi_N
        """
        a_firm.labor_demand = a_firm.desired_output_value * a_firm.labor_productivity
