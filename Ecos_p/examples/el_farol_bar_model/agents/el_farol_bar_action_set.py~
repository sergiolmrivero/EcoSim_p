# -*- coding: utf-8 -*-
""" Basic Strategy Class implementation """

import random


class Strategy:
    """ Implementation of the strategy class """
    def __init__(self):
        self.strategy_name = "general"
        self.strategy = "C"

    def select_game(self):
        return self.select_strategy()

    def select_strategy(self):
        return self.strategy


class AlwaysCooperate(Strategy):
    """ Always Cooperate Strategy """
    def __init__(self):
        self.strategy_name = "cooperate"
        self.strategy = "C"


class AlwaysDefect(Strategy):
    def __init__(self):
        self.strategy_name = "defect"
        self.strategy = "D"


class RandomPlay(Strategy):
    def __init__(self):
        self.strategy_name = "random"
        self.strategy = ["D", "C"]

    def select_strategy(self):
        """ Random Strategy """
        return random.choice(self.strategy)
