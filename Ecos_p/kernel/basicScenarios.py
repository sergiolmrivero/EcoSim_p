#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Scenario
"""
import numpy as np
import datetime as dt
# import yappi #using to profile code


class Scenario(object):
    """
   Class that contains
    the definitions of a scenario
    """
    def __init__(self, simulation, model, name,
                 parameters, variables, agents_init):
        """Initialize a Scenario (with yaml definitions) """
        self.simulation = simulation
        self.model = model
        self.name = name
        self.parameters = parameters
        self.variables = variables
        self.initialize_parameters()
        self.initialize_variables()
        self.agents_init = agents_init
        self.vars_by_agent_type = dict()
        self.agents_of_type = None
        self.vars_dict = dict()
        self.agent_var_name = None
        self.agent_var_type = None
        self.agent_var_dist = None
        self.agent_var_value = None
        self.a_var = None
        self.var_value = None
        self.first = True

    def initialize_parameters(self):
        """
        Initialize the scenario parameters
        The parameters (names and values) come from scenario yaml definition
        """
        for parameter in self.parameters:
            self.parameter_name = parameter['parameter_name']
            self.parameter_value = parameter['parameter_value']
            setattr(self, self.parameter_name, self.parameter_value)

    def initialize_variables(self):
        """
        Initialize scenario variables
        The scenario variables come from the yaml scenario definition
        """
        for variable in self.variables:
            self.variable_name = variable['var_name']
            self.variable_value = variable['var_init_value']
            setattr(self, self.variable_name, self.variable_value)

    def initialize_schedule(self):
        """ Initialize the schedule depending on type of schedule """
        self.schedule = self.model.schedule

    def execute_scenario(self):
        """
        Execute the scenario
        The simulation executes an pre-scenario and a post-scenario for each scenario
        """
        # yappi.start() # init profiling
        self.pre_scenario()
        for run_nr in range(self.no_of_runs):
            if run_nr == 0 or self.reset_each_run:
                self.set_an_agent_vars()
            self.run(run_nr)
        self.post_scenario()
        # yappi.get_func_stats().print_all()  # get statistics
        # yappi.get_thread_stats().print_all()  # get statistics

    def pre_scenario(self):
        """ Initializes the scenario parameters, variable, shcedule, agents vars etc. """
        self.initialize_parameters()
        self.initialize_variables()
        self.initialize_schedule()
        self.initialize_agents_vars()
        self.set_an_agent_vars()

    def run(self, run_nr):
        """
        This method executes the schedule
        """
        # Needs to change to be generic and depedent on the type of scheduling
        self.schedule.execute(self.name,
                              self.step_unit,
                              self.step_interval,
                              self.no_of_steps,
                              run_nr)

    def post_scenario(self):
        """
        In post scenario, the  observation dataframe is saved
        """
        # TODO: Review observer dataframe writing methods (big dataframe consume ram)
        for observer_name, observer in self.model.agent_observers.items():
            observer.create_dataframe()
            self.now = dt.datetime.now().isoformat(timespec='minutes')
            self.filename = "_".join([self.simulation.name,
                                     observer_name,
                                      self.now, '.csv'])
            observer.save_dataframe(self.filename)

    def initialize_agents_vars(self):
        """
        The scenario object initializes the variables dict from the yaml agent
        variables  definition (for each scenario)
        """
        # TODO: This probably will need revision - Using agent pool and simply resetting the agents variable
        #  will be more efficient
        # TODO: This will probably be better to be as a part of the agent class
        for agent_type, agent_vars in self.agents_init.items():
            try:
                self.agents_of_type = None
                self.agents_of_type = self.model.agents_by_type[agent_type]
                if self.agents_of_type is not None:
                    self.vars_dict = dict()
                    for var in agent_vars:
                        self.agent_var_name=var['var_name']
                        self.agent_var_type=var['var_type']
                        self.agent_var_dist=var['var_dist']
                        self.agent_var_value=var['var_value']
                        self.a_var=AgentVar(self.agent_var_name,
                                            self.agent_var_type,
                                            self.agent_var_dist,
                                            self.agent_var_value)
                        self.vars_dict[self.a_var.name] = self.a_var
                        self.vars_by_agent_type[agent_type] = self.vars_dict
            except KeyError:
                print("There is no agent type called ", agent_type,
                      " in this model")

    def set_an_agent_vars(self):
        """ Using the variables dict, the scenario object initializes the variables for each agent (by agent type) """
        for agent_type, agent_vars in self.vars_by_agent_type.items():
            for agent_name, agent in self.model.agents_of_type(agent_type).items():
                for var_name, var in agent_vars.items():
                    self.var_value = var.generate_value()
                    setattr(agent, var_name, self.var_value)


class AgentVar(object):
    """ An agent var """
    def __init__(self, name, var_type, var_dist, value):
        self.name = name
        self.var_type = var_type
        self.dist = var_dist
        self.value = value
        self.generate_value()

    def generate_value(self):
        """ Generates the value for the agent  stochastic variable using the definition in the variable object """
        if self.var_type == 'stochastic':
            self.value = eval(self.dist)
        return self.value
