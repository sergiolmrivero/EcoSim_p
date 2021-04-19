# Rent Market Class  Implementation

from .market import Market


class RentingMarket(Market):
    """ The Renting Market """

    def update(self):
        """ Renting Market updates """
        self.match_bids()
        print("I, the ", self.name, "space: am updating right now")
