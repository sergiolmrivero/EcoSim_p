# Space Labor Market Class  Implementation

from .market import Market


class LaborMarket(Market):
    """ The Labor Market """
    def update(self):
        """ Labor Market updates """
        self.match_bids()
        print("I, the ", self.name, "space: am updating right now")

    def bid_labor_demand(self):
        """ A firm ask for a quantity of labor at a price """
        self.match_bids()

    def pay_salary(self):
        """ Agent pay salaries """
        # TODO: Check if duplicated
        pass

    def pay_wages(self):
        """ Agent pay wages """
        pass

    def contract_gov_labor(self):
        """ Government get household labor """
        pass

    def average_labor_price(self):
        """Labor Market answers the average labor price"""
        self.avg_wage = 0.0
        self.wages = 0.0
        if self.has_offers():
            for value_of_g, labor_offer in self.offers.items():
                self.wages += labor_offer.value_of_g
            self.avg_wage = self.wages / self.no_of_offers()
            return self.avg_wage
        else:
            return 0.0
