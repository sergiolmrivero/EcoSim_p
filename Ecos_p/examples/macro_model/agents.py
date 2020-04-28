# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from basicAgents import DiscreteEventAgent
from spaces import Macro, Market, CG_market, KG_market, Credit_market, Deposits_market
from macro_Caiani_action_set import MacroEcoActionSet
from macro_Caiani_action_set_Goods import GoodsActionSet
from macro_Caiani_action_set_CG import CGActionSet
from macro_Caiani_action_set_Credit import CreditActionSet
from macro_Caiani_action_set_Deposits import DepositsActionSet
from macro_Caiani_action_set_KG import KGActionSet
from macro_Caiani_action_set_Labor import LaborActionSet
from agents_accounting import GoodOrService, CapitalGood
from production import ProductionFunction


class EconomicAgent(DiscreteEventAgent):
    """ A basic economic agent"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)

    def step(self, this_step):
        """ Implemented by subclass"""
        pass


class Household(EconomicAgent):
    """ Household Agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_actions_macro = MacroEcoActionSet()
        self.my_actions_labor = LaborActionSet()

    def step(self, this_step):
        """ Household Agent Step method """
        self.my_step = this_step
        self.my_actions_labor.generate_offer(self)
        self.my_actions_macro.offer_gs(self.my_step,
                                       self.spaces['Labor_market'],
                                       self.labor_offer)
        self.my_actions_macro.show_offer(self,
                                         self.spaces['Labor_market'])

    def show_offer(self):
        """ Show Offer The agent show an offer in some market """
        print(" I, ", self.name,
              "am offering ",
              self.labor_offer.quantity,
              "hour of work at ",
              self.labor_offer.value,
              "hourly wage."
              )


""" A Firm """


class Firm(EconomicAgent):
    """ A Generic Goods Firm"""
    # contracted_labor = {}
    # ready_to_produce = False
    # total_contracted_labor = 0.0

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Initialize a Firm """
        # self.contracted_labor = {}
        # self.ready_to_produce = False
        # self.total_contracted_labor = 0.0
        # self.pf = ProductionFunction(self)
        super().__init__(simulation, model, agent_number, agent_def)

    def step(self, this_step):
        """ Step for the Firm agent """
        # Implemented by subclass
        pass


class CG_Firm(Firm):
    """ A Consumer Goods Firm"""

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Initialize a consumer goods firm """
        super().__init__(simulation, model, agent_number, agent_def)
        self.contracted_labor = {}
        self.ready_to_produce = False
        self.total_contracted_labor = 0.0
        self.pf = ProductionFunction(self)

        self.my_actions_macro = MacroEcoActionSet()
        self.my_actions_labor = LaborActionSet()
        self.my_actions_goods = GoodsActionSet()
        self.my_actions_cg = CGActionSet()

    def step(self, this_step):
        """ Step for the CG agent """
        self.my_step = this_step
        self.my_actions_goods.compute_desired_output(self, 'cg')
        self.my_actions_cg.calculate_labor_demand(self)
        self.my_actions_cg.calculate_capacity_utilization(self)
        self.my_actions_goods.decide_offered_wage(self)
        self.my_actions_labor.contract_labor(self)
        self.my_actions_macro.show_offer(self, self.spaces['Labor_market'])
        if self.ready_to_produce:
            self.output = self.pf.produce(self.desired_output.quantity)
            self.my_actions_macro.offer_gs(self.my_step,
                                           self.spaces['CG_market'],
                                           self.output)
        # self.my_actions_goods.offer_production(self, self.output)
        self.my_actions_goods.sell_production(self)
        self.my_actions_goods.compute_sales_revenue(self)
        self.my_actions_goods.decide_investment(self)
        self.my_actions_goods.contract_credit(self)
        self.my_actions_goods.buy_equipment(self)
        self.my_actions_goods.pay_salaries(self)
        self.my_actions_goods.pay_suppliers(self)
        self.my_actions_goods.pay_interest_bonds(self)
        self.my_actions_goods.pay_interest_loans(self)
        self.my_actions_macro.pay_taxes(self)
        """ A firm adjusts the average wage """
        self.expected_wage = self.my_actions_goods.average_wage(self)

    def show_offer(self):
        """ A cg_firm shows an offer of labor and a desired output """
        print(" I, ", self.name,
              "am getting",
              self.total_contracted_labor,
              "hours of work at ",
              self.my_actions_goods.average_wage(self),
              " average wage, from a total demmand of ",
              self.desired_output.value
              )


class KG_Firm(EconomicAgent):
    """ A Capital Goods Firm"""

    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.contracted_labor = {}
        self.ready_to_produce = False
        self.total_contracted_labor = 0.0
        self.pf = ProductionFunction(self)

        self.my_actions_macro = MacroEcoActionSet()
        self.my_actions_labor = LaborActionSet()
        self.my_actions_goods = GoodsActionSet()
        self.my_actions_kg = KGActionSet()

    def step(self, this_step):
        """ Step for the KG agent """
        self.my_step = this_step
        self.my_actions_goods.compute_desired_output(self, 'kg')
        self.my_actions_goods.decide_offered_wage(self)
        self.my_actions_kg.calculate_labor_demand(self)
        self.my_actions_labor.contract_labor(self)
        # NOTE: Needs to deal with turnover
        self.my_actions_macro.show_offer(self, self.spaces['Labor_market'])
        if self.ready_to_produce:
            self.output = self.pf.produce(self.desired_output.quantity)
            self.my_actions_macro.offer_gs(self.my_step,
                                           self.spaces['KG_market'],
                                           self.output)
        # self.my_actions_goods.produce(self)
        self.my_actions_goods.offer_production(self)
        self.my_actions_goods.sell_production(self)
        self.my_actions_goods.compute_sales_revenue(self)
        self.my_actions_goods.decide_investment(self)
        self.my_actions_goods.contract_credit(self)
        self.my_actions_goods.buy_equipment(self)
        self.my_actions_goods.pay_salaries(self)
        self.my_actions_goods.pay_suppliers(self)
        self.my_actions_goods.pay_interest_bonds(self)
        self.my_actions_goods.pay_interest_loans(self)
        self.my_actions_macro.pay_taxes(self)

    def show_offer(self):
        """ A capital goods firm shows an offer """
        print(" I, ", self.name,
              "am getting",
              self.total_contracted_labor,
              "hours of work at ",
              self.my_actions_goods.average_wage(self),
              " average wage, from a total demmand of ",
              self.desired_output.value
              )


class Bank(EconomicAgent):
    """ A Bank economic agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_actions_macro = MacroEcoActionSet()
        self.my_actions_credit = CreditActionSet()
        self.my_actions_dep = DepositsActionSet()

    def step(self, this_step):
        """ Step method for a bank """
        self.my_step = this_step
        self.cb = self.get_cb()
        self.gov = self.get_government()
        self.my_actions_credit.decide_cr_target(self)
        self.my_actions_credit.decide_interest_rate_strategy(self)
        self.my_actions_credit.offer_credit(self)
        self.my_actions_credit.calculate_exposure(self)
        self.my_actions_credit.receive_advances_CB(self, self.cb, self.ammount)
        self.my_actions_credit.buy_gov_bonds(self, self.gov, self.ammount)
        self.my_actions_macro.pay_taxes(self)
        self.my_actions_macro.show_offer(self, self.spaces['Credit_market'])

    def show_offer(self):
        """ A bank show offer """
        print(" I, ", self.name,
              " am working in this model"
              )

    def get_cb(self):
        """ Get Central Bank from model """
        return self.model.agents_of_type('Central_Bank')

    def get_government(self):
        """ Get government from model """
        return self.model.agents_of_type('Government')


class Government(EconomicAgent):
    """ The Government economic agetn """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_actions_macro = MacroEcoActionSet()
        self.my_actions_credit = CreditActionSet()
        self.my_actions_dep = DepositsActionSet()
        self.my_actions_labor = LaborActionSet()

    def step(self, this_step):
        """ Step method for Government Agent """
        self.my_step = this_step
        self.calculate_available_resources()
        self.my_actions_labor.contract_gov_labor()
        self.my_actions_dep.pay_unempl_benefits()
        self.my_actions_labor.pay_wages()
        self.my_actions_credit.pay_gov_bonds_interest()
        self.my_actions_credit.offer_new_bonds()
        self.my_actions_macro.show_offer(self, self.spaces['Credit_market'])

    def show_offer(self):
        """ Government show offer"""
        print(" I, ", self.name,
              " am working in this model  BCBCBCBBCBCBCBCBCBCBCBCBCBC"
              )

    def calculate_available_resources(self):
        """ Government Calculates Available resources"""
        pass


class Central_Bank(EconomicAgent):
    """ The Central Bank economic agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.my_actions_macro = MacroEcoActionSet()
        self.my_actions_credit = CreditActionSet()
        self.my_actions_dep = DepositsActionSet()

    def step(self, this_step):
        """ Step method for the Central bank Agent """
        self.my_step = this_step
        self.decide_monetary_policy()
        self.my_actions_credit.contract_cash_advances()
        self.my_actions_credit.buy_gov_bonds(self, self.get_government(), self.ammount)
        self.my_actions_dep.transfer_profits_gov()
        self.my_actions_macro.show_offer(self, self.spaces['Credit_market'])

    def show_offer(self):
        """ Central Bank Show Offer """
        print(" I, ", self.name,
              " am working in this model GOVGOVGOVGOVGOVGOVGOVGOVGOV"
              )

    def decide_monetary_policy(self):
        """Central Bank decides monetary policy"""
        pass

    def get_government(self):
        """ Get government from model """
        return self.model.agents_of_type('Government')
