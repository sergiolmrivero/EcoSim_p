# -*- coding: utf-8 -*-

"""
Model Creation

*SLMR


exec(open('macro_Caiani.py').read())

"""
import sys

sys.path.insert(0, '../../kernel')

from simulation import Simulation

macro_sim = Simulation('macro_Caiani_init_test.yaml')
myDumbModel = macro_sim.model

macro_sim.execute_simulation()
