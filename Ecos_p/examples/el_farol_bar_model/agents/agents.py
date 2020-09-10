# -*- coding: utf-8 -*-
""" Agents for the iterated prisioners dilemma model """

from basicAgents import DiscreteEventAgent
from .el_farol_bar_action_set import Strategy, RandomPlay, LikeCrowded


class Player(DiscreteEventAgent):
    """ A basic player in the Iterated Prisioners Dilemma """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.payoff = 0
        self.my_play = ""
        self.other_play = ""
        self.strategy = Strategy()

    def step(self, this_step):
        """ agent step """
        self.select_game()

    def select_game(self):
        """ The agent select a play from a strategy """
        self.my_play = self.strategy.select_game()

    def play(self):
        """ The agent plays a strategy """
        return self.my_play

    def game_payoff(self, perc_frequency):
        """ Get the game payoff """
        self.strategy.get_frequency(perc_frequency)
        self.payoff = self.strategy.payoff()
        print("Agent: ", self.name, "  Payoff: ", self.payoff)


class RandomPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = RandomPlay()


class LikeCrowdedPlayer(Player):
    """ A player that always defect """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.strategy = LikeCrowded()
