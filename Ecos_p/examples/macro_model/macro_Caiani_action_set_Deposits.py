# -*- coding: utf-8 -*-
"""
Deposits Market Action Set
"""

from actions import ActionSet


class DepositsActionSet(ActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space
