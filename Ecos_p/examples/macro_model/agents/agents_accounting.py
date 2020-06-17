#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the accounting module
This module contains all the necessary classes to do
"""
##########################################
# Quais os tipos específicos de bens?
# Que possíveis métodos ainda são necessários???
# Como implementar os protocolos de mercado????
# Ver nd-004 e nd-005
###########################################


class Good(object):
    """A Basic Class representing a good."""
    TYPE = ["real", "financial"]

    """
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

    ASSET_CATEGORY = ['w', 'cg', 'k', 'ph', 'd', 'l', 'id', 'il', 'b', 'ib', 'gw', 'gt']

    CONSUME = ["immediate", "depreciable", "debt", "continuous"]

    def __init__(self, name_of_g,
                 type_of_g,      # real or financial
                 asset_category_of_g,
                 consume_of_g,   # immediate, depreciable, debt or continuous
                 quantity_of_g,
                 value_of_g,
                 owner_of_g=None,
                 producer_of_g=None):
        """" Init method for a generic good """
        self.name_of_g = name_of_g

        if type_of_g in self.TYPE:
            self.type_of_g = type_of_g
        else:
            raise Exception("Type of ", name_of_g, " not valid - type: ", type_of_g)

        if asset_category_of_g in self.ASSET_CATEGORY:
            self.asset_category_of_g = asset_category_of_g
        else:
            raise Exception("Type of asset of :  ", name_of_g, "  not valid - type: ", asset_category_of_g)

        if consume_of_g in self.CONSUME:
            self.consume_of_g = consume_of_g
        else:
            raise Exception("Type of consume from ", name_of_g, " not valid - consume: ", consume_of_g)

        self.quantity_of_g = quantity_of_g
        self.value_of_g = value_of_g
        self.owner_of_g = owner_of_g
        self.producer_of_g = producer_of_g

    def estimated_value(self, a_quantity_of_g):
        """ Calculates the estimated value of a good given a quantity as input """
        return self.value_of_g * a_quantity_of_g

    def total_value(self):
        """ Calculates the estimated value of a good for the existing quantity """
        return self.value_of_g * self.quantity_of_g


# class GoodOrService(object):
#     """
#     A Basic Class representing a good or service.
#     This class includes all types of goods or services of an economy
#     Types of Goods:
#         w  - Wages
#         cg - Consumer_Good
#         k  - Capital
#         ph - Dividends
#         d  - Deposit
#         l  - Loan
#         id - Interests on deposits
#         il - Interests on loans
#         b  - Bonds
#         ib - Interests on bonds
#         gw - Government wages
#         gt - Government transfers (to households)
#     """

# # ==============================================================================
# # It probably will be necessary to specialize this class to include the
# # specificities of the different goods or services.
# # Type of specific goods that will probably need more detail:
# #   - Capital
# #   - Labor (Available_labour???) - How to treat it as a service?
# #   - Financial Assets and Liabilities (see how to include interests)
# #
# # ==============================================================================

#     def __init__(self, name_of_gs, type_of_gs, quantity_of_gs,
#                  value_of_gs,
#                  asset_owner_of_gs=None,
#                  liability_owner_of_gs=None):
#         """ Init method for a Good (or service) """
#         self.name = name_of_gs
#         self.gs_type = type_of_gs
#         self.value = value_of_gs
#         self.quantity = quantity_of_gs
#         self.asset_owner = asset_owner_of_gs
#         self.liability_owner = liability_owner_of_gs

#     def estimated_value(self, a_quantity_of_gs):
#         """ Calculates the estimated value of a good given a quantity as input """
#         return self.value * a_quantity_of_gs

#     def total_value(self):
#         """ Calculates the estimated value of a good for the existing quantity """
#         return self.value * self.quantity


# class CapitalGood(GoodOrService):
#     """ Capital Good represents production equipment
#         Its used to produce consumer goods
#     """
#     def __init__(self, name_of_gs,
#                  quantity_of_gs,
#                  value_of_gs,
#                  asset_owner_of_gs=None,
#                  liability_owner_of_gs=None):
#         """ Initialize a production (capital) good """
#         self.name = name_of_gs
#         self.gs_type = "k"
#         self.value = value_of_gs
#         self.quantity = quantity_of_gs
#         self.asset_owner = asset_owner_of_gs
#         self.liability_owner = liability_owner_of_gs
#         self.capital_productivity = 0.5
#         self.labor_productivity = 0.5
