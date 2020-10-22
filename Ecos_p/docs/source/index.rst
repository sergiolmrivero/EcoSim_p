.. EcoSim_p documentation master file, created by
   sphinx-quickstart on Thu Oct 22 14:18:13 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

EcoSim_p: An ABM simulation tool in Python
===========================================

Economic Simulation in Python (EcoSim_p) is an agent based modelling and simulation framework made in Python 3+. The models are written in python but all te initialization and definition of the interface are in json.

EcoSim_p Design Patterns
------------------------

EcoSim_p uses MVC, dependency injection and other design patterns to implement the simulation.

The framework is constructed around a kernel module and has examples to show the use of the model.




.. toctree::
   :hidden:
   :maxdepth: 7

   Kernel <apis/kernel>
   El Farol Bar <apis/examples.el_farol_bar_model>
   IPD <apis/examples.ipd_model>
   Macro Model <apis/examples.macro_model>
   Modules <apis/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
