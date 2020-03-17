#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Scenario

*SLMR
"""
import numpy as np
import datetime as dt
import yappi


class Scenario(object):
    """
   Class that contains
    the definitions of a scenario
    """
    def __init__(self, simulation, model, name,
                 parameters, variables, agents_init):
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
        for parameter in self.parameters:
            self.parameter_name = parameter['parameter_name']
            self.parameter_value = parameter['parameter_value']
            setattr(self, self.parameter_name, self.parameter_value)

    def initialize_variables(self):
        for variable in self.variables:
            self.variable_name = variable['var_name']
            self.variable_value = variable['var_init_value']
            setattr(self, self.variable_name, self.variable_value)

    def initialize_schedule(self):
        """ Initialize the schedule depending on type of schedule """
        self.schedule = self.model.schedule

    def execute_scenario(self):
        yappi.start()
        self.pre_scenario()
        for run_nr in range(self.no_of_runs):
            if run_nr == 0 or self.reset_each_run:
                self.set_an_agent_vars()
            self.run(run_nr)
        self.post_scenario()
        yappi.get_func_stats().print_all()
        yappi.get_thread_stats().print_all()

    def pre_scenario(self):
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
        for observer_name, observer in self.model.agent_observers.items():
            observer.create_dataframe()
            self.now = dt.datetime.now().isoformat(timespec='minutes')
            self.filename = "_".join([self.simulation.name,
                                     observer_name,
                                      self.now, '.csv'])
            observer.save_dataframe(self.filename)

    # def initialize_agents_vars(self):
    #     np.random.seed()
    #     for agent_type, agent_vars in self.agents_init.items():
    #         try:
    #             self.agents_of_type = None
    #             self.agents_of_type = self.model.agents_by_type[agent_type]
    #             if self.agents_of_type is not None:
    #                 for agent in self.agents_of_type.values():
    #                     self.vars_dict = dict()
    #                     for var in agent_vars:
    #                         self.agent_var_name = var['var_name']
    #                         self.agent_var_type = var['var_type']
    #                         self.agent_var_dist = var['var_dist']
    #                         self.agent_var_value = var['var_value']
    #                         self.a_var = AgentVar(self.agent_var_name,
    #                                               self.agent_var_type,
    #                                               self.agent_var_dist,
    #                                               self.agent_var_value)
    #                         self.vars_dict[self.a_var.name] = self.a_var
    #                         # self.vars_by_agent_type[agent_type] = self.vars_dict
    #                         self.var_value = self.a_var.generate_value()
    #                         setattr(agent, self.a_var.name, self.var_value)
    #                         # self.set_an_agent_vars(agent)
    #         except KeyError:
    #             print("There is no agent type called ", agent_type,
    #                   " in this model")

    def initialize_agents_vars(self):
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
                        self.vars_dict[self.a_var.name]=self.a_var
                        self.vars_by_agent_type[agent_type] = self.vars_dict
            except KeyError:
                print("There is no agent type called ", agent_type,
                      " in this model")

    def set_an_agent_vars(self):
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
        if self.var_type == 'stochastic':
            self.value = eval(self.dist)
        return self.value
