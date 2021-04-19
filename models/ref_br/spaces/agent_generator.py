# -*- coding: utf-8 -*-
"""Agent Generator """

from basicSpaces import Space

class HouseholdGenerator(Space):
    """
    
        The household generator agent

        Each step this agent generates a quantity of agents
        creating new agents in the simulation
        
    """

    def __init__(self, model, name, actions_set_file, action_class, variables):
        """ Intializes the Household Generator """
        super().__init__(model, name, actions_set_file, action_class, variables)
        self.first = True

    def update(self):
        """ The creation of households """
        if self.first:
            self.no_of_households = self.model.agents_of_type_number("Household")
            self.first = False

        self.hh_to_create = self.birth_rate
        for n in range(self.hh_to_create):
            self.model.create_one_agent("Household")