# -*- coding: utf-8 -*-

"""
Model Creation

*exec(open('macro_Caiani.py').read())


SLMR

"""
import sys
#import yappi

sys.path.insert(0, '../../kernel')

from Ecos_p.kernel.simulation import Simulation

macro_sim = Simulation('macro_Caiani.yml')
eco_m = macro_sim.model
#yappi.start()
macro_sim.execute_simulation()

#yappi.get_func_stats().print_all()
#yappi.get_thread_stats().print_all()
