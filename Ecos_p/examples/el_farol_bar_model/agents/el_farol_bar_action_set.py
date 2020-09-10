# -*- coding: utf-8 -*-
""" Basic Strategy Class implementation """

import random


class Strategy:
    """ Implementation of the strategy class """

    STRATEGY = ['GOING', 'NOT GOING']

    def __init__(self):
        """ Init the strategy of the agent """
        self.strategy_name = "general"
        self.strategy = self.STRATEGY[0]
        self.perc_frequency = {'GOING': 0.9,
                               'NOT GOING': 0.1}

    def select_game(self):
        return self.select_strategy()

    def select_strategy(self):
        return self.strategy

    def get_frequency(self, perc_frequency):
        """ The strategy gets the current frequency in the bar """
        self.perc_frequency['GOING'] = perc_frequency['GOING']
        self.perc_frequency['NOT GOING'] = perc_frequency['NOT GOING']

    def payoff(self):
        """ Specialized by subclass """
        return random.random()


class LikeCrowded(Strategy):
    """  Strategy Like Crownded """
    def __init__(self):
        super().__init__()
        self.strategy_name = "likeCrowded"
        self.strategy = self.STRATEGY[0]

    def select_strategy(self):
        """ Like Crownded Strategy """
        if self.perc_frequency['GOING'] > 0.6:
            self.strategy = self.STRATEGY[0]
        else:
            self.strategy = self.STRATEGY[1]

        return self.strategy


class LikeSixtyPercent(Strategy):
    """ Strategy under sixty percent """
    def __init__(self):
        super().__init__()
        self.strategy_name = "likeSixtyPercent"
        self.strategy = self.STRATEGY[1]


class RandomPlay(Strategy):
    """ Strategy under random """
    def __init__(self):
        super().__init__()
        self.strategy_name = "random"

    def select_strategy(self):
        """ Random Strategy """
        return random.choice(self.STRATEGY)


class PredictionModel:
    """ The prediction model that the agent uses to choose the strategy """

    def __init__(self):
        """ Init the strategy of the agent """
        self.model_name = "no_prediction"
        self.expected_frequency = 0.6
        self.observed_frequeincy = 0.0

    def make_prediction(self):
        """ The prediction based on the model """
        self.expected_frequency = random.random()
