# -*- coding: utf-8 -*-
"""
Dumb Model Action Set
"""

from actions import ActionSet


class MacroEcoActionSet(ActionSet):
    """ Coomon actitons for the economic model """
    def form_expectations(self, step, z_t_1, z_e_t_1, lmbda):
        """ The agent forms zie expectation using
            the following equation:
                z^e = z^e_{t-1} + lambda(z_{t-1} - z^e_{t-1})
                where: z is the value of the voi and lambda(lmbda)
                       is the impact of the variable of interest
                       in the expectation.
        """
        z_e = z_t_1 + lmbda * (z_t_1 - z_e_t_1)
        return(z_e)

    def offer_gs(self, step, market, gs):
        market.offers[gs.value] = gs

    def has_offers(self, market):
        if market.offers.__len__() > 0:
            return True
        else:
            return False

    def no_of_offers(self, market):
        return market.offers.__len__()

    def get_lowest_offer(self, market):
        self.key, self.value = market.offers.popitem(0)
        return self.value

    def get_highest_offer(self, market):
        self.key, self.value = market.offers.popitem(-1)
        return self.value

    def return_offer(self, market, gs):
        self.offer_gs(market, gs)

    def show_offer(self, an_agent, market):
        """ Show offer """
        an_agent.show_offer()
        print("")
        print("Model: ", an_agent.model.name)
        print("------------")

    def compute_production_price(self):
        " Agent compute production price"
        pass


    def pay_taxes(self, an_agent):
        """ An agent pay taxes """
        pass
