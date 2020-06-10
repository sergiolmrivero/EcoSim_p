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

    def produce(self, goods_quantity):
        """ Produce using labor and equipment """
        self.quantity_to_produce = goods_quantity
        self.produced_quantity = 0
        self.production_not_finished = True
        while self.production_not_finished:
            self.produce_goods()
        return self.produced_goods

    def produce_goods(self):
        """ Private Method - Produce goods """
        # Needs Implementation
        self.produced_quantity = self.quantity_to_produce
        self.production_value = self.calculate_production_value()
        self.production_not_finished = False
        self.produced_goods = Good('consumer_good',
                                   'real',
                                   'cg',
                                   'immediate',
                                   self.produced_quantity,
                                   self.production_value,
                                   self.owner,
                                   self.owner)

    def calculate_production_value(self):
        """ Calculates the production value """
        # Needs implementation
        return 10.0


class Equipment:
    """
    The equipment used in the production function
    """
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
