.. A description of the interface

**************************************
Iterated Prisioners' Dilemma Tutorial
**************************************

The iterated prisioners' dilemma is a classic game that was implemented as a tournament. 


The app directory structure
###########################

In the *examples* folder, we have the *ipd_model* folder that have our simple implementation of the **ipd game**.

Here is the strucuture of the app files and folders. This is a typical directory structure of an app.


.. image:: ../images/app_dir_stru.png
   :alt: Folders structure of a typical app

Folders structure of a typical app


The Agents and Actions
######################



Action Set
==========

First we create the actions module that we call *ipd_action_set.py*

In this module, we create a class  *Game* to represent a game.


.. code-block:: python

   class Game:
       """ Class Representing a Game """

       def __init__(self, my_name=None, my_play=None, my_payoff=None,
                    other_name=None, other_play=None, other_payoff=None):
           self.my_name = my_name
           self.my_play = my_play
           self.my_payoff = my_payoff
           self.other_name = other_name
           self.other_play = other_play
           self.other_payoff = other_payoff

This class just implements the data structures what will be used in a typical game by the agent.


After, we implement a class named *Strategy* this class will be specialized to implement the different strategies.

The basic implementation of the *Strategy* class is:

.. code-block:: python

    class Strategy:
	""" Implementation of the strategy class """
	def __init__(self):
	    self.strategy_name = "general"
	    self.strategy = "C"
	    self.game = Game("", "C", 3, "", "C", 3)
	    self.last_game = Game("", "C", 3, "", "C", 3)

	def select_game(self):
	    return self.strategy

	def update_game(self, aGame):
	    """ Get a game """
	    self.last_game = copy.copy(self.game)
	    self.game = aGame


The basic strategy has a name, a variable to store the strategy (**C** for *cooperate* and **D** to *defect*), the actual *game* (a *Game* object) and the *last_game* (another *Game* object).

After that we implement two very simple self explaining strategies , *AlwaysCooperate* and *AlwaysDefect*.

.. code-block:: python

    class AlwaysCooperate(Strategy):
	""" Always Cooperate Strategy """
	def __init__(self):
	    super().__init__()
	    self.strategy_name = "cooperate"
	    self.strategy = "C"


    class AlwaysDefect(Strategy):
	def __init__(self):
	    super().__init__()
	    self.strategy_name = "defect"
	    self.strategy = "D"


Then we implement a *RandomPlay* strategy:

.. code-block:: python

    class RandomPlay(Strategy):
	def __init__(self):
	    super().__init__()
	    self.strategy_name = "random"
	    self.strategy = ["D", "C"]

	def select_game(self):
	    """ Random Strategy """
	    return random.choice(self.strategy)

To do that we need to import the *random* module in the file (**import random**).

Finally we implement the *SimpleTitForTat* strategy:

.. code-block:: python

    class SimpleTitForTat(Strategy):
	def __init__(self):
	    super().__init__()
	    self.strategy_name = "simpleTitForTat"
	    self.other_last_strategy = "C"
	    self.selected_strategy = "C"

	def select_game(self):
	    """ Simple Tit for tat strategy """
	    if self.last_game.other_play == "C":
		self.selected_strategy = "C"
	    else:
		self.selected_strategy = "D"

	    return self.selected_strategy


	    
Agents
======
   
The agents of our model are implemented in the *agents.py* module. We usually include an *agents* folder to have the app organized. The agents can be implemented in more than one module, so, is good to have all agents in a separated sub-folder.

.. code-block:: python
		
   # -*- coding: utf-8 -*-
   """ Agents for the iterated prisioners dilemma model """

   from basicAgents import DiscreteEventAgent
   from .ipd_action_set import Strategy, AlwaysCooperate, AlwaysDefect, RandomPlay, SimpleTitForTat, Game


   class Player(DiscreteEventAgent):
       """ A basic player in the Iterated Prisioners Dilemma """
       def __init__(self, simulation, model, agent_number, agent_def):
	   super().__init__(simulation, model, agent_number, agent_def)
	   self.my_payoff = 0
	   self.my_play = "C"
	   self.other_name = ""
	   self.other_play = "C"
	   self.other_payoff = 0
	   self.strategy = Strategy()
	   self.game = Game(self.name, "C", 3, "", "C", 3)
	   self.strategy.update_game(self.game)

       def step(self):
	   """ The agent selects a play from a strategy """
	   self.my_play = self.strategy.select_game()

       def play(self):
	   """ The agent plays a strategy """
	   return self.my_play

       def game_payoff(self, other_name, other_play, other_payoff, my_payoff):
	   """ Get the game payoff """
	   self.my_payoff = my_payoff
	   self.other_name = other_name
	   self.other_play = other_play
	   self.other_payoff = other_payoff
	   self.game.my_payoff = my_payoff
	   self.game.other_name = other_name
	   self.game.other_play = other_play
	   self.game.other_payoff = other_payoff
	   self.strategy.update_game(self.game)
	   # print("ag name: ", self.name, "play: ", self.my_play, "payoff: ", self.my_payoff)


This is the basic implementation of the agent.

The agent has the variables to the plays and payoffs, a *Game* object and an *Strategy* object, that will implement the agent strategy.


The agent *step* method just set the agent strategy.

The *play* method will be used to communicate the agent strategy in the *GameSpace* in an asynchronous way.


Now we implement the specific agents. There will be one agent subclass for each different strategy.


.. code-block:: python

   class GoodPlayer(Player):
       """ A player that always cooperate """
       def __init__(self, simulation, model, agent_number, agent_def):
	   super().__init__(simulation, model, agent_number, agent_def)
	   self.strategy = AlwaysCooperate()


   class BadPlayer(Player):
       """ A player that always defect """
       def __init__(self, simulation, model, agent_number, agent_def):
	   super().__init__(simulation, model, agent_number, agent_def)
	   self.strategy = AlwaysDefect()


   class RandomPlayer(Player):
       """ A player that always defect """
       def __init__(self, simulation, model, agent_number, agent_def):
	   super().__init__(simulation, model, agent_number, agent_def)
	   self.strategy = RandomPlay()


   class TitForTatPlayer(Player):
       """ A player that always defect """
       def __init__(self, simulation, model, agent_number, agent_def):
	   super().__init__(simulation, model, agent_number, agent_def)
	   self.strategy = SimpleTitForTat()


The *TitForTat* agent has a tit-for-tat strategy. This implements the agent behavior.


Spaces
######

The spaces folder contains the spaces. Again we separate the spaces in a sub-folder because we could have more than one space and this is a way to organize the app.

.. code-block:: python

   # -*- coding: utf-8 -*-
   """ Basic IPD game space implementation """

   from basicSpaces import Space


   class IpdGame(Space):
       """ Abstract Market """
       STRATEGY = ['C', 'D']
       PAYOFFS = {'CC': [3, 3],
		  'CD': [0, 5],
		  'DC': [5, 0],
		  'DD': [1, 1]}

       def __init__(self, model, name, actions_set_file, action_class):
	   """ Intialize abstract market """
	   super().__init__(model, name, actions_set_file, action_class)

       def update(self):
	   """ here the players play the game """
	   agents = list(self.model.mixed_agents())
	   half = len(agents) // 2
	   players1 = agents[:half]
	   players2 = agents[half:]
	   for player1 in players1:
	       if len(players2) > 0:
		   player2 = players2.pop()
		   p1 = player1.play()
		   p2 = player2.play()
		   game = p1 + p2
		   player1.game_payoff(player2.name, p2,
				       self.PAYOFFS[game][1],
				       self.PAYOFFS[game][0]
				       )
		   player2.game_payoff(player1.name,
				       p1, self.PAYOFFS[game][0],
				       self.PAYOFFS[game][1]
				       )
	       else:
		   player1.game_payoff("NA", 0)


The *IpdGame* class is a subclass of *basicSpaces* from the *EcoSim_p* Kernel module. There is only one method for this class, the method *update*.

In this method  (called by the *Schedule*), the space mix randomly the agents, separate them  in two and play one agent from the first half with other agent from the second half until there is no agents to play.

There is a Dictionary *PAYOFFS* that contains the payoffs to each pair of strategies played by the agents in each iteration.


Defining the Simulations
########################

In the *ipd.json* file we define the initialization, the agents in the game, the spaces, the observers, the scenarios and the initialization of the variables of the agents (in each scenario).


.. code-block:: json

   {
     "simulation_name": "ipd",
     "simulation_parameters": [
       {
	 "parameter_name": "total_payoff",
	 "parameter_value": 0.0
       }
     ],
     "model_name": "ipd",
     "schedule": [
       {
	 "schedule_type": "MixedSchedule",
	 "schedule_name": "MyMxSchd"
       }
     ],
     "spaces": [
	 {
	   "space_type": "IpdGame",
	   "space_name": "IpdGame",
	   "action_set": "ipd_action_set",
	   "action_class": "Strategy",
	   "space_variables": {
	       "payoffs": 0.0
	   }
       }
     ],
     "agents": [
       {
	 "agent_type": "GoodPlayer",
	 "agent_prefix": "GPl",
	 "agent_spaces": [
	     "IpdGame"
	 ],
	   "no_of_agents": 20
       },
       {
	 "agent_type": "BadPlayer",
	 "agent_prefix": "BPl",
	 "agent_spaces": [
	     "IpdGame"
	 ],
	 "no_of_agents": 20
       },
       {
	 "agent_type": "RandomPlayer",
	 "agent_prefix": "RPl",
	 "agent_spaces": [
	     "IpdGame"
	 ],
	 "no_of_agents": 20
       },
       {
	 "agent_type": "TitForTatPlayer",
	 "agent_prefix": "TTPl",
	 "agent_spaces": [
	     "IpdGame"
	 ],
	 "no_of_agents": 20
       }

     ],
     "observers": [
       {
	 "observer_type": "Observer",
	 "observer_name": "GPObs",
	 "observer_actions": [
	   "obs_gpl"
	 ],
	 "observer_agent": "GoodPlayer",
	 "observable_vars": [
	     "my_payoff",
	     "my_play",
	     "other_name",
	     "other_play",
	     "other_payoff"
	 ]
       },
       {
	 "observer_type": "Observer",
	 "observer_name": "BPObs",
	 "observer_actions": [
	   "obs_bpl"
	 ],
	 "observer_agent": "BadPlayer",
	 "observable_vars": [
	     "my_payoff",
	     "my_play",
	     "other_name",
	     "other_play",
	     "other_payoff"
	 ]
       },
       {
	 "observer_type": "Observer",
	 "observer_name": "RObs",
	 "observer_actions": [
	   "obs_bpl"
	 ],
	 "observer_agent": "RandomPlayer",
	 "observable_vars": [
	     "my_payoff",
	     "my_play",
	     "other_name",
	     "other_play",
	     "other_payoff"
	 ]
       },
       {
	 "observer_type": "Observer",
	 "observer_name": "TTObs",
	 "observer_actions": [
	   "obs_bpl"
	 ],
	 "observer_agent": "TitForTatPlayer",
	 "observable_vars": [
	     "my_payoff",
	     "my_play",
	     "other_name",
	     "other_play",
	     "other_payoff"
	 ]
       }

     ],
     "scenarios": [
       {
	 "scenario_type": "Scenario",
	 "scenario_name": "Scenario1",
	 "scenario_parameters": [
	   {
	     "parameter_name": "no_of_runs",
	     "parameter_value": 10
	   },
	   {
	     "parameter_name": "reset_each_run",
	     "parameter_value": true
	   },
	   {
	     "parameter_name": "step_unit",
	     "parameter_value": "step"
	   },
	   {
	     "parameter_name": "step_interval",
	     "parameter_value": 1
	   },
	   {
	     "parameter_name": "no_of_steps",
	     "parameter_value": 100
	   }
	 ],
	 "scenario_variables": [
	   {
	     "var_name": "payoffs",
	     "var_init_value": 0.0,
	     "var_type": "sharp"
	   }
	 ],
	 "agents_init": {
	   "GoodPlayer": [
	       {
		   "var_name": "payoff",
		   "var_type": "integer",
		   "var_dist": "none",
		   "var_value": 1
	       }
	   ],
	   "BadPlayer": [
	       {
		   "var_name": "payoff",
		   "var_type": "integer",
		   "var_dist": "none",
		   "var_value": 1
	       }
	   ],
	   "RandomPlayer": [
	       {
		   "var_name": "payoff",
		   "var_type": "integer",
		   "var_dist": "none",
		   "var_value": 1
	       }
	   ],
	   "TitForTatPlayer": [
	       {
		   "var_name": "payoff",
		   "var_type": "integer",
		   "var_dist": "none",
		   "var_value": 1
	       }
	   ]

	 }
       }
     ]
   }
