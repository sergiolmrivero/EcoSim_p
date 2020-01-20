# -*- coding: utf-8 -*-
"""
Capital Goods Market Action Set
"""

from actions import ActionSet


class KGActionSet(ActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space

    def decide_investment(self):
        "Agent CG firm decides investment"
        pass

    def buy_equipment(self):
        "Agent CG_firm buys equipment"
        pass
