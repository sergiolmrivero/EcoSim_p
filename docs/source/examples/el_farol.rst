.. El Farol Bar problem example


The El Farol Bar Problem
========================

The `El Farol Bar Problem`_ is a *tought experiment* proposed by Brian-Arthur in 1994 that intends to show the emergent properties of a complex system.

.. _`El Farol Bar Problem` : http://tuvalu.santafe.edu/~wbarthur/elfarol.htm

The patrons of a bar (The *El Farol Bar*, in Santa Fe, New Mexico) want to go to the bar, but are not happy if the bar is crowded. So, each agent have multiple forecast models that she/he/they uses to estimate the probable bar attendance and decide to go (or not) to the bar.

The concurrent methods of forecast compete and the method that have the best fitness is chosen, so the agents change the forecast methods according with the accuracy of the observed predictions.

This problem was later generalized by In 1997 Damien Challet and Yi-Cheng Zhang into game form as the **Minority Game**.

We have implemented an `example of the El Farol Bar problem`_.

.. _`example of the El Farol Bar problem` :  ../apis/examples.el_farol_bar_model.html

The model is executed using a .sh file **el_farol_classic.sh** that runs the model and the *R markdown* file `El_Farol.rmd`_ that generates the report with the simulation results that can be seen in this `html file`_ as a sample of a typical run of the simulation

.. _`El_Farol.rmd` : ../_static/El_Farol.rmd
.. _`html file` : ../_static/El_Farol.html




To execute the model go to the El Farol Bar Model folder (examples/el_farol_bar_model) Open a bash console and write:

.. code-block:: bash
		
    $ ./el_farol_classic.sh
 

The results will be show in a browser (look for the file El_Farol.html in the folder **'results'**)


.. toctree::
   :hidden:
   :maxdepth: 7

   example of the El Farol Bar problem <../apis/examples.el_farol_bar_model>
