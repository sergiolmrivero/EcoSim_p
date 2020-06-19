# -*- coding: utf-8 -*-
""" El Farol Bar space implementation """

from basicSpaces import Space


class EFBGame(Space):
    """ Abstract Market """

    STRATEGY = ['GOING', 'NOT GOING']

    def __init__(self, model, name, actions_set_file, action_class):
        """ Intialize abstract market """
        super().__init__(model, name, actions_set_file, action_class)
        self.frequency = {'GOING': 0,
                          'NOT GOING': 0}
        self.perc_frequency = {'GOING': 0.0,
                               'NOT GOING': 0.0}

    def update(self):
        """ Implemented by subclass - Testing update """
        self.play()

    def play(self):
        """ here the players play the game """
        self.collect_strategies()
        self.calculate_frequency()
        self.notify_frequency()

    def collect_strategies(self):
        """ The Space Get the agents decisions """
        for agent in self.model.mixed_agents():
            agent_strategy = agent.play()
            if agent_strategy == self.STRATEGY[0]:
                self.frequency['GOING'] += 1
            elif agent_strategy == self.STRATEGY[1]:
                self.frequency['NOT GOING'] += 1
            else:
                print("Wrong Strategy. Agent: ", agent.name, " Strategy: ", agent_strategy)

    def calculate_frequency(self):
        """ Space calculates the frequency of the agents """
        number_of_agents = self.model.agents_number()
        self.perc_frequency['GOING'] = self.frequency['GOING'] / number_of_agents
        self.perc_frequency['NOT GOING'] = self.frequency['NOT GOING'] / number_of_agents

    def notify_frequency(self):
        """ The space notify the agents about the frequency """
        for agent in self.model.agents.values():
            agent.game_payoff(self.perc_frequency)
