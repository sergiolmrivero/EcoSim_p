# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from basicAgents import DiscreteEventAgent


class EconomicAgent(DiscreteEventAgent):
    """ A basic economic agent"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.contracted_offers = {}
        self.demmand_satisfied = False

    def step(self, this_step):
        """ Implemented by subclass"""
        pass

    def get_contracted_offers(self, contracted_offers):
        """ The agent get the contracted_offers """
        self.contracted_offers = contracted_offers
        self.demmand_satisfied = True
