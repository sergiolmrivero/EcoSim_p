# Space Class  Implementation
from basicSpaces import Space
from sortedcontainers import SortedDict
# TODO: Check which methods for the Action sets are better here


class Market(Space):
    """ Abstract Market """
    def __init__(self, model, name, actions_set_file, action_class):
        """ Intialize abstract market """
        super().__init__(model, name, actions_set_file, action_class)
        self.offers = SortedDict()

    def init_offers(self, new_offers):
        """ Get new offers dict and check if is a sorted dict - if yes, set it """
        if isinstance(new_offers, SortedDict):
            self.offers = new_offers
        else:
            print('The input is not a sorted dictionary')
