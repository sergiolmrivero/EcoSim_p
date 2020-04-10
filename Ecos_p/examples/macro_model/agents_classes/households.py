# -*- coding: utf-8 -*-
""" Household Agent """

from EconomicAgent import Economic_Agent
from accounting import GoodOrService


class Household(Economic_Agent):
    """ A Household"""
    def step(self, this_step):
        self.my_step = this_step
        self.generate_offer()
        self.offer_workforce()
        self.actions['show_offer'](self,
                                   self.spaces['Labor_market'])

    def decide_hourly_wage(self):
        """ The Household decides wage to offer """
        self.hourly_wage = self.expected_wage

    def generate_offer(self):
        """ The Household decides wage to offer """
        self.decide_hourly_wage()
        self.labor_offer = GoodOrService(self.name, 'w',
                                         self.labor_capacity,
                                         self.hourly_wage,
                                         asset_owner_of_gs=self)

    def offer_workforce(self):
        """ The household offer some work """
        self.actions['offer_gs'](self.my_step,
                                 self.spaces['Labor_market'],
                                 self.labor_offer)

    def show_offer(self):
        print(" I, ", self.name,
              "am offering ",
              self.labor_offer.quantity,
              "hour of work at ",
              self.labor_offer.value,
              "hourly wage."
              )
