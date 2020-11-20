.. Iterated Prisoners' Dilemma example


The Iterated Prisoners' Dilemma
===============================

The `prisoners' dilemma`_  is a classic Game Theory problem that had an implementation from `Robert Axelrod`_ and David Hamilton intended to discuss the `evolution of cooperation`_.

.. _`prisoners' dilemma` : https://plato.stanford.edu/entries/prisoner-dilemma/
.. _`Robert Axelrod` : http://www-personal.umich.edu/~axe/
.. _`evolution of cooperation` : http://www-personal.umich.edu/~axe/research/Axelrod%20and%20Hamilton%20EC%201981.pdf

Here we implement a simple version of the `IPD game`_

.. _`IPD game` :  ../apis/examples.ipd_model.html

The model is executed using a .sh file **ipd.sh** that runs the model and the *R markdown* file `ipd.rmd`_ that generates the report with the simulation results that can be seen in this `html file`_ as a sample of a typical run of the simulation

.. _`ipd.rmd` : ../_static/ipd.rmd
.. _`html file` : ../_static/ipd.html




To execute the model go to the IPD Model folder (*examples/ipd_model*) Open a bash console and write:

.. code-block:: bash
		
    $ ./ipd.sh
 

The results will be show in a browser (look for the file *ipd.html* in the folder **'results'**)


.. toctree::
   :hidden:
   :maxdepth: 7

   IPD game :  <../apis/examples.ipd_model>
