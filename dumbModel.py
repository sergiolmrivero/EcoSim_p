# -*- coding: utf-8 -*-

"""
Model Creation

*SLMR


exec(open('dumbModel.py').read())

"""
from simulation import Simulation
import basicSpaces
import basicAgents
import model

import agents
import spaces

dumbSim = Simulation('simulation_init.yaml')
myDumbModel = dumbSim.model

dumbSim.execute_simulation()