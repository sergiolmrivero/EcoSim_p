#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the accounting module
This module contains all the necessary classes to do
"""


class GoodOrService(object):
    """
    A Basic Class representing a good or service.
    This class includes all types of goods or services of an economy
    Types of Goods:
        w  - Wages
        cg - Consumer_Good
        k  - Capital
        ph - Dividends
        d  - Deposit
        l  - Loan
        id - Interests on deposits
        il - Interests on loans
        b  - Bonds
        ib - Interests on bonds
        gw - Government wages
        gt - Government transfers (to households)
    """

# ==============================================================================
# It probably will be necessary to specialize this class to include the
# specificities of the different goods or services.
# Type of specific goods that will probably need more detail:
#   - Capital
#   - Labor (Available_labour???) - How to treat it as a service?
#   - Financial Assets and Liabilities (see how to include interests)
#
# ==============================================================================

    def __init__(self, name_of_gs, type_of_gs, quantity_of_gs,
                 value_of_gs,
                 asset_owner_of_gs=None,
                 liability_owner_of_gs=None):
        self.name = name_of_gs
        self.gs_type = type_of_gs
        self.value = value_of_gs
        self.quantity = quantity_of_gs
        self.asset_owner = asset_owner_of_gs
        self.liability_owner = liability_owner_of_gs

    def estimated_value(self, a_quantity_of_gs):
        return self.value * a_quantity_of_gs

    def total_value(self):
        return self.value * self.quantity


class CapitalGood(GoodOrService):
    """ Capital Good represents production equipment
        Its used to produce consumer goods
    """
    def __init__(self, name_of_gs,
                 quantity_of_gs,
                 value_of_gs,
                 asset_owner_of_gs=None,
                 liability_owner_of_gs=None):
        self.name = name_of_gs
        self.gs_type = "k"
        self.value = value_of_gs
        self.quantity = quantity_of_gs
        self.asset_owner = asset_owner_of_gs
        self.liability_owner = liability_owner_of_gs
        self.capital_productivity = 0.5
        self.labor_productivity = 0.5