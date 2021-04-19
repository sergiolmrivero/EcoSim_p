# Space Class  Implementation

from .market import Market


class RealStateMarket(Market):
    """ The Real State Market """

    def match_bids(self):
        """
        Market matching of offer and demand
        This method can be specialized depending on  market
        Is prepared to be an assincronous method
        This method here is specialized to the RE market
        """
        self.bids_not_matched = True
        self.contracted_offer = None
        self.total_contracted_value = 0.0
        self.excess_demand = self.total_demands()

        while self.bids_not_matched:
            if self.has_demand():
                self.a_demand = self.get_highest_demand()
                self.demand_not_satisfied = True
                self.demand_owner = self.a_demand.owner_of_g
                self.total_contracted_value = 0.0

                while self.demand_not_satisfied:
                    if self.has_offers():
                        self.an_offer = self.get_highest_offer()
                        if self.a_demand.value_of_g >= self.an_offer.value_of_g:
                            self.an_offer.owner_of_g = self.demand_owner
                            self.contracted_offer = self.an_offer
                            self.total_contracted_value += self.an_offer.value_of_g                      
                            self.demand_not_satisfied = False
                            self.notify_match(self.a_demand, self.contracted_offer)
                            self.register_contract(self.a_demand, self.contracted_offer)
                    else:
                        self.demand_not_satisfied = False
                        self.release_demand()
                        self.demand.clear()
            else:
                self.bids_not_matched = False
                self.release_offers()
                self.offers.clear()

    def notify_match(self, a_demand, contracted_offer):
        """ Notify the agents that their bids where matched """
        self.contractor = a_demand.owner_of_g
        self.contractor.get_contracted_offers(contracted_offer)
        contracted_offer.producer_of_g.got_contract(contracted_offer)

    
class SPRealStateMarket(RealStateMarket):
    """ SP Real State Market """


class RJRealStateMarket(RealStateMarket):
    """ RJ Real State Market """

        