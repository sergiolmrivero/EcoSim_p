# Space Class  Implementation
from basicSpaces import Space
from sortedcontainers import SortedDict


class Market(Space):
    """ Abstract Market """
    def __init__(self, model, name, actions_set_file, action_class):
        super().__init__(model, name, actions_set_file, action_class)
        self.offers = SortedDict()

    def init_offers(self, new_offers):
        if isinstance(new_offers, SortedDict):
            self.offers = new_offers
        else:
            print('The input ins not a sorted dictionary')


class Labor_market(Market):
    """ The Labor Market"""


class CG_market(Market):
    """ The Consumer Goods Market"""


class KG_market(Market):
    """ The Capital Goods Market"""


class Credit_market(Market):
    """ The Credit Market"""


class Deposits_market(Market):
    """ The Deposits Market"""
