# -*- coding: utf-8 -*-
"""
Capital Goods Market Action Set
"""

from macro_Caiani_action_set_goods import GoodsActionSet
from accounting import GoodOrService

class KGActionSet(GoodsActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space
    
    def compute_desired_output_kg(self, a_kg_firm):
        """Agent compute desired output"""
        
        a_kg_firm.desired_output_kg = GoodOrService(a_kg_firm.name, 'kg',
                                             a_kg_firm.desired_output,
                                             a_kg_firm.expected_price,
                                            a_kg_firm)

    def decide_offered_wage_kg(self, a_kg_firm):
        """
        Decide the wage for the quantity of expected
        work that firm wants to contract
        """
        a_kg_firm.offered_wage = a_kg_firm.expected_wage

    def contract_labor_kg(self, a_kg_firm):
        """
        Trabalho total contratado precisa ser ajustado.
        """
        offers_available = True
        print(a_kg_firm.actions['no_of_offers'](a_kg_firm.spaces['Labor_market']))
        while offers_available:
            if a_kg_firm.actions['has_offers'](a_kg_firm.spaces['Labor_market']):
                a_kg_firm.an_offer = a_kg_firm.actions['get_lowest_offer'](a_kg_firm.spaces['Labor_market'])
                a_kg_firm.offer_owner = a_kg_firm.an_offer.asset_owner
                a_kg_firm.contracted_labor[a_kg_firm.offer_owner] = a_kg_firm.an_offer
                a_kg_firm.total_contracted_labor += a_kg_firm.an_offer.value
                if a_kg_firm.total_contracted_labor >= a_kg_firm.desired_output:
                    a_kg_firm.ready_to_produce = True
                    offers_available = False
                else:
                    offers_available = False
                    print("Labor Market has no offers")
                    
    def average_wage(self, a_kg_firm):
        wages = 0
        workers = len(a_kg_firm.contracted_labor)
        if workers > 0:
            for labor_offer in a_kg_firm.contracted_labor.values():
                wages += labor_offer.value
                avg_wage = wages / workers
        else:
            avg_wage = 0
        return avg_wage

    def produce_kg(self, a_kg_firm):
        """ produce """
        pass

    def offer_production_kg(self, a_kg_firm):
        "Agent offer production of consumer goods"
        pass

    def sell_production_kg(self, a_kg_firm):
        "KG_firm sells production"
        pass

    def compute_sales_revenue_kg(self, a_kg_firm):
        "Agent compute sells of CG"
        pass

    def decide_investment_kg(self, a_kg_firm):
        pass
    
    def contract_credit_kg(self, a_kg_firm):
        pass
    
    def buy_equipment_kg(self, a_kg_firm):
        pass
    
    def pay_salaries_kg(self, a_kg_firm):
        pass
    
    def pay_suppliers_kg(self, a_kg_firm):
        pass

    def pay_interest_bonds_kg(self, a_kg_firm):
        pass

    def pay_interest_loans_kg(self, a_kg_firm):
        pass
    
    def pay_taxes_kg(self, a_kg_firm):
        pass
    