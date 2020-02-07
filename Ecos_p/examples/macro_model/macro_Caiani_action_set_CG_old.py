# -*- coding: utf-8 -*-
"""
Consumer Goods Action Set
"""


from macro_Caiani_action_set_goods import GoodsActionSet
from accounting import GoodOrService

class CGActionSet(GoodsActionSet):
    """ Dumb model action set """
    def __init__(self, model, space):
        self.model = model
        self.space = space
    
    def compute_desired_output_cg(self, a_cg_firm):
        """Agent compute desired output"""
        
        a_cg_firm.desired_output_cg = GoodOrService(a_cg_firm.name, 'cg',
                                             a_cg_firm.desired_output,
                                             a_cg_firm.expected_price,
                                            a_cg_firm)

    def decide_offered_wage_cg(self, a_cg_firm):
        """
        Decide the wage for the quantity of expected
        work that firm wants to contract
        """
        a_cg_firm.offered_wage = a_cg_firm.expected_wage

    def contract_labor_cg(self, a_cg_firm):
        """
        Trabalho total contratado precisa ser ajustado.
        """
        offers_available = True
        print(a_cg_firm.actions['no_of_offers'](a_cg_firm.spaces['Labor_market']))
        while offers_available:
            if a_cg_firm.actions['has_offers'](a_cg_firm.spaces['Labor_market']):
                a_cg_firm.an_offer = a_cg_firm.actions['get_lowest_offer'](a_cg_firm.spaces['Labor_market'])
                a_cg_firm.offer_owner = a_cg_firm.an_offer.asset_owner
                a_cg_firm.contracted_labor[a_cg_firm.offer_owner] = a_cg_firm.an_offer
                a_cg_firm.total_contracted_labor += a_cg_firm.an_offer.value
                if a_cg_firm.total_contracted_labor >= a_cg_firm.desired_output:
                    a_cg_firm.ready_to_produce = True
                    offers_available = False
                else:
                    offers_available = False
                    print("Labor Market has no offers")
                    
    def average_wage(self, a_cg_firm):
        wages = 0
        workers = len(a_cg_firm.contracted_labor)
        if workers > 0:
            for labor_offer in a_cg_firm.contracted_labor.values():
                wages += labor_offer.value
                avg_wage = wages / workers
        else:
            avg_wage = 0
        return avg_wage

    def produce_cg(self, a_cg_firm):
        """ produce """
        pass

    def offer_production_cg(self, a_cg_firm):
        "Agent offer production of consumer goods"
        pass

    def sell_production_cg(self, a_cg_firm):
        "CG_firm sells production"
        pass

    def compute_sales_revenue_cg(self, a_cg_firm):
        "Agent compute sells of CG"
        pass

    def decide_investment_cg(self, a_cg_firm):
        pass
    
    def contract_credit_cg(self, a_cg_firm):
        pass
    
    def buy_equipment_cg(self, a_cg_firm):
        pass
    
    def pay_salaries_cg(self, a_cg_firm):
        pass
    
    def pay_suppliers_cg(self, a_cg_firm):
        pass

    def pay_interest_bonds_cg(self, a_cg_firm):
        pass

    def pay_interest_loans_cg(self, a_cg_firm):
        pass
    
    def pay_taxes_cg(self, a_cg_firm):
        pass
    