# -*- coding: utf-8 -*-
""" Firm Agents from the basic macroeconomic model """

from .agents import EconomicAgent

from .agents_accounting import Good

from .production import ProductionFunction


# A Firm

class Firm(EconomicAgent):
    """ A Generic Goods Firm"""

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Initialize a Firm """
        super().__init__(simulation, model, agent_number, agent_def)

    def step(self, this_step):
        """ Step for the Firm agent """
        # Implemented by subclass
        pass

    def show_offer(self):
        """ A firm shows an offer of labor and a desired output """
        print(" I, ", self.name,
              "am getting",
              self.total_contracted_labor,
              "hours of work at ",
              self.average_wage(),
              " average wage, from a total demmand of ",
              self.desired_output.value_of_g
              )

    def form_expectations(self, step, z_t_1, z_e_t_1, lmbda):
        """ The agent forms zie expectation using
            the following equation:
                z^e = z^e_{t-1} + lambda(z_{t-1} - z^e_{t-1})
                where: z is the value of the voi and lambda(lmbda)
                       is the impact of the variable of interest
                       in the expectation.
        """
        z_e = z_t_1 + lmbda * (z_t_1 - z_e_t_1)
        return (z_e)

    def decide_offered_wage(self):
        """
        Decide the wage for the quantity of expected
        work that firm wants to contract
        """
        """ The Household decides wage to offer """
        self.offer_wage = self.labor_market.average_labor_price()
        if self.offer_wage == 0.0:
            self.offer_wage = self.expected_wage

    def average_wage(self):
        """ A firm answers the average wage for contracted labor """
        return self.labor_market.average_labor_price()

    def generate_demmand(self):
        """ The Firm decides the labor demmand """
        # Check if labor demmand is gt labor contracted
        # Or if contracts are expired

        self.labor_demand_g = Good('Labor',
                                   'real',
                                   'w',
                                   'immediate',
                                   self.labor_demand,
                                   self.offer_wage,
                                   self,
                                   self)

    def calculate_contracted_labor(self):
        """ The firm calculates the contracted labor """
        self.total_contracted_labor = 0.0
        if self.demmand_satisfied:
            for worker, labor in self.contracted_offers.items():
                self.total_contracted_labor += labor.quantity_of_g

    def pay_salaries(self):
        """ A firm pay the salaries """
        pass


class CGFirm(Firm):
    """ A Consumer Goods Firm"""

    def __init__(self, simulation, model, agent_number, agent_def):
        """ Initialize a consumer goods firm """
        super().__init__(simulation, model, agent_number, agent_def)
        self.total_contracted_labor = 0.0
        self.pf = ProductionFunction(self)
        self.labor_market = self.spaces['LaborMarket']
        self.cg_market = self.spaces['CGMarket']

    def step(self, this_step):
        """ Step for the CG agent """
        self.my_step = this_step
        self.compute_desired_output()
        self.calculate_labor_demand()
        self.calculate_capacity_utilization()
        self.labor_market.bid_market('D', self.labor_demand_g)
        if self.demmand_satisfied:
            self.calculate_contracted_labor()
            self.show_offer()
            self.output = self.pf.produce(self.desired_output)
            self.pay_salaries()
            self.cg_market.offer_gs(self.output)
        # self.my_actions_goods.offer_production(self, self.output)
        self.cg_market.sell_production(self)
        self.cg_market.compute_sales_revenue(self)
        self.cg_market.decide_investment(self)
        self.cg_market.contract_credit(self)
        self.cg_market.buy_equipment(self)
        self.cg_market.pay_salaries(self)
        self.cg_market.pay_suppliers(self)
        self.cg_market.pay_interest_bonds(self)
        self.cg_market.pay_interest_loans(self)
        self.cg_market.pay_taxes(self)
        """ A firm adjusts the average wage """
        self.expected_wage = self.average_wage()

    def calculate_capacity_utilization(self):
        """
        A CG Firm calculates capacity_utilization using capital productivity and
        the firm's capital stock
        """
        self.capacity_utilization = min(1, (self.desired_output_value
                                            / (self.capital_stock
                                               * self.capital_productivity)))

    def calculate_labor_demand(self):
        """
        A CG Firm calculates the total label demmand for production (NDct)
        This is calculated the using real capital stock for firm (kct) and the
        capital labor ratio for the specific technology (lk).
        NDct = kct/lk
        """
        self.labor_demand = (self.capacity_utilization
                             * (self.capital_stock
                                / self.capital_labor_ratio))
        self.decide_offered_wage()
        self.generate_demmand()

    def compute_desired_output(self):
        """
        A firm compute desired output
        The firm computes the inventory percentage that it can maintain
        and the desired output from the expected sales and inventory
        """
        self.desired_perc_inv = self.inventory / self.expected_sales
        self.desired_output_value = (self.expected_sales
                                     * (1 + self.desired_perc_inv)
                                     - self.inventory_t_1)
        self.desired_output = Good('consumer_good',
                                   'real',
                                   'cg',
                                   'immediate',
                                   self.desired_output_value,
                                   self.expected_price,
                                   self,
                                   self)


class KGFirm(Firm):
    """ A Capital Goods Firm"""

    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.ready_to_produce = False
        self.total_contracted_labor = 0.0
        self.pf = ProductionFunction(self)
        self.labor_market = self.spaces['LaborMarket']
        self.kg_market = self.spaces['KGMarket']

    def step(self, this_step):
        """ Step for the KG agent """
        self.my_step = this_step
        self.compute_desired_output()
        self.calculate_labor_demand()
        self.labor_market.bid_market('D', self.labor_demand_g)
        # NOTE: Needs to deal with turnover
        if self.ready_to_produce:
            self.calculate_contracted_labor()
            self.show_offer()
            self.output = self.pf.produce(self.desired_output.quantity_of_g)
            self.kg_market.offer_gs(self.output)
        self.kg_market.offer_production(self)
        self.kg_market.sell_production(self)
        self.kg_market.compute_sales_revenue(self)
        self.kg_market.decide_investment(self)
        self.kg_market.contract_credit(self)
        self.kg_market.buy_equipment(self)
        self.kg_market.pay_salaries(self)
        self.kg_market.pay_suppliers(self)
        self.kg_market.pay_interest_bonds(self)
        self.kg_market.pay_interest_loans(self)
        self.kg_market.pay_taxes(self)

    def calculate_labor_demand(self):
        """
        A KG Firm calculates the total label demmand for production (NDct)
        This is calculated the using desired output (yD_kt) and the
        labor productivity (mi_N)
        NDct = yD_kt/mi_N
        """
        self.labor_demand = self.desired_output.value_of_g * self.labor_productivity
        self.decide_offered_wage()
        self.generate_demmand()

    def compute_desired_output(self):
        """
        A firm compute desired output
        The firm computes the inventory percentage that it can maintain
        and the desired output from the expected sales and inventory
        """
        self.desired_perc_inv = self.inventory / self.expected_sales
        self.desired_output_value = (self.expected_sales
                                     * (1 + self.desired_perc_inv)
                                     - self.inventory_t_1)
        self.desired_output = Good('capital_good',
                                   'real',
                                   'k',
                                   'depreciable',
                                   self.desired_output_value,
                                   self.expected_price,
                                   self,
                                   self)
