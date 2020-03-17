# -*- coding: utf-8 -*-

"""
Model Creation

*SLMR


exec(open('dumb_model.py').read())

"""
import sys

sys.path.insert(0, '../../kernel')

from simulation import Simulation

dumbSim = Simulation('dumb_model_init.yml')
myDumbModel = dumbSim.model

dumbSim.execute_simulation()
