# -*- coding: utf-8 -*-
"""
Credit Market Action Set
"""
from actions import ActionSet


class CreditActionSet(ActionSet):
    """ Credit space action set """

    def decide_cr_target(self, a_bank):
        """ A bank agent decides capital ratio target """
        pass

    def decide_interest_rate_strategy(self, a_bank):
        """A bank decides the strategy for interest rate determination """
        pass

    def offer_credit(self, a_bank):
        """ A bank offer credit on the credit market """
        pass

    def contract_credit(self, an_agent, a_bank):
        """ An agent contracts credit from a Bank """
        pass

    def calculate_exposure(self, a_bank):
        """ A bank calculates its exposure """
        pass

    def contract_cash_advances(self):
        """ Central Bank Contract Cash Advances on the Credit Market """
        pass

    def receive_advances_CB(self, a_bank, central_bank, ammount):
        """ A bank receive some ammount of money  from the central bank at some interest rate """
        pass

    def buy_gov_bonds(self, a_bank, gov, ammount):
        """ A bank buy government bonds """
        pass

    def pay_gov_bonds_interest(self):
        """ A government pays bonds and interests """
        pass

    def offer_new_bonds(self):
        """ A government offers bonds """
        pass
