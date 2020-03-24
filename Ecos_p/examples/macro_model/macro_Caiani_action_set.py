# -*- coding: utf-8 -*-
"""
Macro Model Action Set
"""

from actions import ActionSet


class MacroEcoActionSet(ActionSet):
    # TODO: maybe this methods belongs to the market in the market protocol implementation
    """ Common actions for the economic model """
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
        """ include an  offer in the market """
        market.offers[gs.value] = gs

    def has_offers(self, market):
        """ A market answers if is has offers (True or False) """
        if market.offers.__len__() > 0:
            return True
        else:
            return False

    def no_of_offers(self, market):
        """ A market answers the number of offers it has """
        return market.offers.__len__()

    def get_lowest_offer(self, market):
        """ A market answers the offer with the lowest value (in the market.offers ordered dict) """
        self.key, self.value = market.offers.popitem(0)
        return self.value

    def get_highest_offer(self, market):
        """ A market answers the offer with the highest value (in the market.offers ordered dict) """
        self.key, self.value = market.offers.popitem(-1)
        return self.value

    def return_offer(self, market, gs):
        """ A market receives an offer of a good or service """
        self.offer_gs(market, gs)

    def show_offer(self, an_agent, market):
        """ Show offer """
        an_agent.show_offer()
        print("")
        print("Model: ", an_agent.model.name)
        print("------------")

    def compute_production_price(self):
        """ Agent compute production price """
        pass

    def pay_taxes(self, an_agent):
        """ An agent pay taxes """
        pass
