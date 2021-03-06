# -*- coding: utf-8 -*-
""" Firm Agents from the basic macroeconomic model """

from numpy import random
from numpy.lib.shape_base import column_stack

from .agents import EconomicAgent

from .agents_accounting import Good, House



# A Firm

class Firm(EconomicAgent):
    """ A Generic Goods Firm"""

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Initialize a Firm """
        super().__init__(simulation, model, agent_number, agent_def)

    def step(self):
        """ Step for the Firm agent """
        # Implemented by subclass
        pass

  

class ConstructionFirm(Firm):
    """ A Construction Firm"""

    MARKET = 'REMarket'
    MARKET_NAME = 'ConstructionFirm'

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Initialize a consumer goods firm """
        super().__init__(simulation, model, agent_number, agent_def)
        self.first = True
        self.offered_houses = dict()
        self.my_market = self.spaces[self.MARKET]
        self.previous_demand = 0

    def step(self):
        """ Step for the CG agent """
        if self.first:
            self.generate_first_offer()
            self.first = False
        
        self.form_expectations()
        self.generate_offer()
        self.update_statistics()
        

    def generate_first_offer(self):
        """ The Construction Firm Generates its first offer """
        for i in range(1,self.housing_offer):
            house_name = "h_" + str(i)
            self.generate_house(house_name)
            

    def form_expectations(self):
        """ 
            The agent establish its expectations about the demmand 
        """
        not_sold_houses = self.offered_houses.__len__()
        self.actual_demand = self.housing_demand - not_sold_houses
        initial_number = self.housing_demand
        if self.my_market.excess_demand > 0:
            max_offer = self.my_market.excess_demand
        else:
            max_offer = self.housing_demand
                
        if self.actual_demand == self.housing_demand:
            new_offer_no = self.housing_demand + random.randint(0,max_offer)
            for i in range(1, new_offer_no):
                house_nr = initial_number + i
                house_name = "nhhd_" + str(house_nr)
                house = self.generate_house(house_name)
                house.mark_up = house.mark_up * (1 + random.normal(0.2, 0.05))
                house.value_of_g = house.cost + (1 + house.mark_up)
        else:
            new_offer_no = self.actual_demand - not_sold_houses
            for i in range(1, new_offer_no):
                house_nr = initial_number + i
                house_name = "nhld_" + str(house_nr)
                house = self.generate_house(house_name)
                house.mark_up = house.mark_up / (1 + random.normal(0.2, 0.05))
                house.value_of_g = house.cost + (1 + house.mark_up)
        
        self.previous_demand = self.actual_demand
        self.housing_demand = self.housing_offer = self.offered_houses.__len__()
            
    def generate_offer(self):
        """ The construction firm generates the number of houses in the REM """
        for house in self.offered_houses.values():
            self.my_market.bid_market("O", house)
    
    def generate_house(self, house_name):
        """ 
            Returns a house price 
            A price is price plus mark_up.
        """
        self.scenario.initialize_one_var("house_cost", 
                                         self.MARKET_NAME,
                                         self)
        self.scenario.initialize_one_var("mark_up", 
                                         self.MARKET_NAME,
                                         self)
        self.house_price = self.house_cost * (1 + self.mark_up) 
        house = House(house_name,
                          value_of_g=self.house_price,
                          owner_of_g=self, 
                          producer_of_g=self
                          )
        
        house.cost = self.house_cost
        house.mark_up = self.mark_up
        self.offered_houses[house.name_of_g] = house
        
        return house

    def got_contract(self, contracted_offer):
        """ the agent got a contract for an offer """
        self.offer_accepted = True
        self.contracted_offer = contracted_offer
        house_name = contracted_offer.name_of_g
        bought_house = self.offered_houses.pop(house_name)
        self.revenue += bought_house.value_of_g

    def update_statistics(self):
        """ Update some variables """
        s_mark_up = 0
        s_cost = 0
        s_price = 0
        for house_name, house in self.offered_houses.items():
            s_mark_up += house.mark_up
            s_cost += house.cost
            s_price += house.value_of_g
        
        offered_houses_n = self.offered_houses.__len__()
        if offered_houses_n > 0:
            self.avg_mark_up = s_mark_up/offered_houses_n
            self.avg_house_cost = s_cost/offered_houses_n
            self.avg_house_price = s_price/offered_houses_n
        else:
            self.avg_mark_up = s_mark_up/1
            self.avg_house_cost = s_cost/1
            self.avg_house_price = s_price/1
        self.total_house_cost = s_cost


class SPConstructionFirm(ConstructionFirm):
    """ Construction firm for the SP Market """
    MARKET = 'SPREMarket'
    MARKET_NAME = 'SPConstructionFirm'



class RJConstructionFirm(ConstructionFirm):
    """ Construction firm for the RJ Market """
    MARKET = 'RJREMarket'
    MARKET_NAME = 'RJConstructionFirm'
