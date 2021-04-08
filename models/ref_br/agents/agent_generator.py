# -*- coding: utf-8 -*-
"""Agent Generator """

from basicAgents import DiscreteEventAgent
import random

class HouseholdGenerator(DiscreteEventAgent):
    """
    
        The household generator agent

        Each step this agent generates a quantity of agents
        creating new agents in the simulation
        
    """

    def __init__(self, simulation, model, agent_number, agent_def) -> None:
        super().__init__(simulation, model, agent_number, agent_def)
        """ Intializes the Household Generator """
        

    def step(self):
        """ The creation of households """
        #self.hh_to_create = self.birth_rate
        #for n in range(self.hh_to_create):
        #    self.model.create_one_agent("Household")
        pass