# -*- coding: utf-8 -*-
""" Household Agent """

from EconomicAgent import Economic_Agent
from accounting import GoodOrService


class CG_Firm(Economic_Agent):
    """ A Consumer Goods Firm"""
    contracted_labor = dict()
    ready_to_produce = False
    total_contracted_labor = 0.0

    def step(self, this_step):
        self.my_step = this_step
        self.compute_expected_output()
        self.decide_offered_wage()
        self.contract_labor()
        self.actions['show_offer'](self, self.spaces['Labor_market'])
        if self.ready_to_produce:
            self.produce()

    def compute_expected_output(self):
        """Agent compute desired output"""
        self.expected_output = GoodOrService(self.name, 'cg',
                                             self.desired_output,
                                             self.expected_price,
                                             asset_owner_of_gs=self)

    def decide_offered_wage(self):
        """
        Decide the wage for the quantity of expected
        work that firm wants to contract
        """
        self.offered_wage = self.expected_wage

    def contract_labor(self):
        """
        Trabalho total contratado precisa ser ajustado.
        """
        offers_available = True
        print(self.actions['no_of_offers'](self.spaces['Labor_market']))
        while offers_available:
            if self.actions['has_offers'](self.spaces['Labor_market']):
                self.an_offer = self.actions['get_lowest_offer'](self.spaces['Labor_market'])
                self.offer_owner = self.an_offer.asset_owner
                self.contracted_labor[self.offer_owner] = self.an_offer
                self.total_contracted_labor += self.an_offer.value
                if self.total_contracted_labor >= self.desired_output:
                    self.ready_to_produce = True
                    offers_available = False
                else:
                    offers_available = False
                    print("Labor Market has no offers")

    def average_wage(self):
        wages = 0
        workers = len(self.contracted_labor)
        if workers > 0:
            for labor_offer in self.contracted_labor.values():
                wages += labor_offer.value
                avg_wage = wages / workers
        else:
            avg_wage = 0
        return avg_wage

    def produce(self):
        """ produce """
        pass

    def show_offer(self):
        print(" I, ", self.name,
              "am getting",
              self.total_contracted_labor,
              "hours of work at ",
              self.average_wage(),
              " average wage, from a total demmand of ",
              self.desired_output
              )
