.. EcoSim_p documentation master file, created by
   sphinx-quickstart on Thu Oct 22 14:18:13 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

******************************************
EcoSim_p: An ABM simulation tool in Python
******************************************


Economic Simulation in Python (EcoSim_p) is an agent based modeling and simulation framework made in Python 3+. The models are written in python but all te initialization and definition of the interface are in json.

EcoSim_p Design Patterns
########################

EcoSim_p uses MVC, dependency injection and other design patterns to implement the simulation.

The framework is constructed around a kernel module and has examples to show the use of the model.


Structure
#########

The framework is composed by three parts:

- **Interface** - Is the view part of the simulator, and is accessed by html/css files. From this pages the user can define the initial parameters of a simulation, run and visualize a simulation.
- **Kernel** - Is the main part of the simulator. In the kernel we have all the control of the simulator. A simulation is created executing the __*main.py*__, with the model definition files (json) passed as parameters.
- **Apps** - The apps are the implementations of the models. Each model has its folder  and subfolders. The definition of the simulation intialization is in a json file and the agents, spaces and actions in the model are defined in specific python modules.


.. image:: images/Structure_Ecos_p.png
   :alt: Graphical Representation of the Kernel and App components of the framework


Main Features
=============

* `Kernel design principles`_

* `Interface`_
  
* `Json Files`_
	 

.. _`Kernel design principles` : concepts/kernel.html

.. _`Interface` : concepts/interface.html

.. _`Json Files` : concepts/json_files.html
	   



Getting Started
===============

To obtain the kernel and examples you can go in the folowing github page:

* `EcoSim_p`_

.. _`EcoSim_p` : https://github.com/sergiolmrivero/EcoSim_p


Or alternatively you can clone the framework using github client, or other clonning method:

.. code-block:: bash

    $ gh repo clone sergiolmrivero/EcoSim_p



Tutorial
========

Agents

ActionSet

Spaces

Exectution


Examples
========

* `El-Farol Bar Problem`_

* `Iterated Prisioners Dilemma`_

* `Macroeconomic Model`_


.. _`El-Farol Bar Problem` : examples/el_farol.html
.. _`Iterated Prisioners Dilemma` : examples/ipd.html
.. _`Macroeconomic Model` : examples/macro_caiani.html

Roadmap
=======

Parallel Execution

Integration with R and Jupyter





.. toctree::
   :hidden:
   :maxdepth: 7

   Kernel <apis/kernel>
   El Farol Bar <apis/examples.el_farol_bar_model>
   IPD <apis/examples.ipd_model>
   Macro Model <apis/examples.macro_model>
   Modules <apis/modules>
   Kernel design principles <concepts/kernel.rst>
   Interface <concepts/interface.rst>
   Json Files <concepts/json_files.rst>
   El-Farol Bar Problem : <examples/el_farol.rst>
   Iterated Prisioners Dilemma : <examples/ipd.rst>
   Macroeconomic Model : <examples/macro_caiani.rst>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
