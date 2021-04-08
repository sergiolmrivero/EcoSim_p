# Housing Market Class  Implementation

from .market import Market


class HousingMarket(Market):
    """ The Housing Market """

    def update(self):
        """ Housing Market updates """
        self.match_bids()
        print("I, the ", self.name, "space: am updating right now")


