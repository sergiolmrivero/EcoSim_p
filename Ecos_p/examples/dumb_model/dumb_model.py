# -*- coding: utf-8 -*-

"""
Model Creation

*SLMR


exec(open('dumb_model.py').read())

"""
import sys

from simulation   import Simulation
from model  import Model
from basicSpaces import Space
from basicAgents import Agent


import agents
import spaces

sys.path.insert(0, '../../kernel')

dumbSim = Simulation('dumb_model_init.yaml')
myDumbModel = dumbSim.model

dumbSim.execute_simulation()

