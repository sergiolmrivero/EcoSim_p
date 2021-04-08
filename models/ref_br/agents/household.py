# -*- coding: utf-8 -*-
""" Household Agents from the basic macroeconomic model """

from .agents import EconomicAgent
from .agents_accounting import Good, House
import random


class Household(EconomicAgent):
    """ Household Agent """

    H_REL = ['social','renter', 'owner', 'investor']
    SPACE = 'REMarket'


    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.first_step = True
        self.house = House("house",owner_of_g=None, producer_of_g=None)
        self.demanded_house = House("house",owner_of_g=self, producer_of_g=self)
        self.my_market = self.spaces[self.SPACE]
    

    def step(self):
        """ Household Agent Step method """
        if self.first_step:
            #self.my_ownership = random.choices(self.house_ownership,
            #                                   self.ownership_probability)
            self.house_ownership = "renter"
            self.my_house_type = random.choices(self.house.QUALITY,
                                               self.house_type_probability)
            self.house.quality = self.my_house_type
            
            ## demand house
            self.demanded_house.quality = self.my_house_type
            self.demanded_house.value_of_g = self.savings
            self.first_step = False


        self.update_demography()
        self.calculate_income()
        self.consume()
        self.housing_decision()
        self.generate_offer()
        self.got_house()
        self.pay_contracts()
        self.pay_taxes()
        self.check_survivability()

    def update_demography(self):
        """ The household instance updates demographic variables 
            Families are born, die and leave an inheritance. 
            There is a constant birth rate and age and 
            income distribution appropriate to the analyzed reality. 
            When one family dies, another family is chosen at random 
            to inherit property and wealth.
        """
        self.age += 1
    
    def check_survivability(self):
        """Check if the agent will die using probability and age"""
        pass
        #for index, age_interval in enumerate(self.age_group):
        #    age_range = range(age_interval[0],age_interval[1])
        #    agrng = self.age in age_range
        #    if self.age in age_range:
        #        if self.death_probability[index]*random.random() > 0.999:
        #            self.dead()

        
        #if random.random() > 0.99:
        #    self.dead()

    def calculate_income(self):
        """ Households receive income according to 
        an appropriate distribution throughout life and age"""
        change = random.gauss(0,0.02)
        if(change < 0):
            self.income *= (1 - change)
        else:
            self.income *= (1 + change)

    def consume(self):
        """Households use a percentage of income in essential consumption"""
        self.consumption = self.income * self.consumption_rate
        self.savings += self.income * (1 - self.consumption_rate)

    def housing_decision(self):

    
        """ Households decide on housing following this protocol:
            1) Whether in a “social house” or if the contract has ended, 
            they decide between buying or renting a new house.

            2) If they rent they keep paying. There is no breach of 
            contract between the parties.

            3) If you are an owner, that is, you occupy a house, you
            decide whether to sell and buy a new house or move to rent.

            4) If they have the investor DNA, they decide whether 
            to buy new properties, and for each property 
            they decide whether to sell or rent.

            5) Families that want to buy or rent houses place their offers 
            on the respective markets (property or rent). 
            
            6) Families who also decide to sell or rent their homes 
            also place their offers on the markets.
        """
        # TODO: This is very complex 
        #       - Maybe to separate in multiple methods
    
    def generate_offer(self):
        "Agent generates offer"
        if self.house_ownership == 'renter':
            self.demanded_house.value_of_g = self.savings
            self.my_market.bid_market("D", self.demanded_house)


    def got_house(self):
        ### Tem erro aqui - CHECAR
        """ The household have bought a house """
        if self.demand_satisfied and self.house_ownership != 'owner':
            self.house = self.contracted_offers
            self.house.owner_of_g = self
            self.savings -= self.house.value_of_g
            self.house_ownership = 'owner'


    def pay_contracts(self):
        """ Tenants pay rent. Owners with financing pay the bank. """
        pass

    def formulate_price_expectations(self):
        """ The household formulates price expectations for consumer goods """
        pass

    def pay_taxes(self):
        """ The HH pay taxes to the government """
        pass

    def got_contract(self):
        """ The household bought a house """
    pass

    def release_bid(self):
        """ The agent have a house """
        pass


class SPHousehold(Household):
    """ Household from the SP REM"""

    H_REL = ['social','renter', 'owner', 'investor']
    SPACE = 'SPREMarket'

    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        

class RJHousehold(Household):
    """ Household from the RJ REM"""
    H_REL = ['social','renter', 'owner', 'investor']
    SPACE = 'RJREMarket'

    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
