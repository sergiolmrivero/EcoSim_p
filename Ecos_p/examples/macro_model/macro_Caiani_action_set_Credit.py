# -*- coding: utf-8 -*-
"""
Credit Market Action Set
"""

from actions import ActionSet


class CreditActionSet(ActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space
