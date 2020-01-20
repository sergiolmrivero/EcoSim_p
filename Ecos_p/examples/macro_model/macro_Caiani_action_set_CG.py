# -*- coding: utf-8 -*-
"""
Consumer Goods Action Set
"""


from macro_Caiani_action_set import MacroEcoActionSet


class CGActionSet(MacroEcoActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space

    def offer_production(self):
        "Agent offer production of consumer goods"
        pass

    def sell_production(self):
        "CG_firm sells production"
        pass

    def compute_sales_revenue(self):
        "Agent compute sells of CG"
        pass
