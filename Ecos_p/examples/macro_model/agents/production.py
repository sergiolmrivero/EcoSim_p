#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The production Functions for the Firms

@author: rivero

"""

from .agents_accounting import Good


class ProductionFunction:
    """
    The production function class is used by the firms to produce.
    """
    # TODO: Especifica de maneira mais completa a função de produção.
    def __init__(self, firm):
        """ Initialize class with labor and equipment """
        self.owner = firm
        self.labor = []
        self.equipment = []
        self.quantity_to_produce = 0
        self.produced_quantity = 0
        self.production_not_finished = False

    def add_equipment(self, a_capital_good):
        """ Ad an equipment to the firm production capacity """
        self.equipment[a_capital_good.name] = a_capital_good

    def get_contracted_labor(self, firm_contracted_labor):
        """ Get all contracted labor to produce """
        self.labor = firm_contracted_labor

    def produce(self, goods):
        """ Produce using labor and equipment """
        # TODO: O componente de capital precisa ser feito.
        # TODO: A função de produção precisa ser rescrita de maneira a corresponde ao esquema teórico de produção
        self.goods_to_produce = goods
        self.produced_quantity = 0
        self.produced_goods = Good(self.goods_to_produce.name_of_g,
                                   self.goods_to_produce.type_of_g,
                                   self.goods_to_produce.asset_category_of_g,
                                   self.goods_to_produce.consume_of_g,
                                   self.goods_to_produce.quantity_of_g,
                                   self.goods_to_produce.value_of_g,
                                   self.owner,
                                   self.owner)
        return self.produced_goods


class Equipment:
    """
    The equipment used in the production function
    """
    # TODO: Equipamento (e a produtividade do equipamento, precisam entrar n função 
    def __init__(self, owner, K=None, Y_L=None, Y_P=None, L_P=None, Y=None, L=None):
        """ Create Equipment"""
        self.owner = owner
        self.K = K
        self.Y_L = Y_L
        self.Y_P = Y_P
        self.L_P = L_P
        self.Y = Y
        self.L = L

    def produce(self, Y):
        """ Production """
        pass
