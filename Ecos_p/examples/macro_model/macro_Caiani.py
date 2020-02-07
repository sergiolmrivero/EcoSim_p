# -*- coding: utf-8 -*-

"""
Model Creation

*exec(open('macro_Caiani.py').read())


SLMR

"""
import sys

sys.path.insert(0, '../../kernel')

from simulation import Simulation

macro_sim = Simulation('macro_Caiani.yaml')
eco_m = macro_sim.model

macro_sim.execute_simulation()
