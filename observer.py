#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of the class Observer
Inspired on datacollection.py from mesa abm
https://mesa.readthedocs.io/en/master/
*SLMR
"""

import dependency_injector.providers as providers
import dependency_injector.errors as errors
import pandas as pd
import datetime as dt


class Observer(object):
    """ Schedule Class
        Um Agente pode estar em varios espaços...Mas o observador do agente é DO AGENTE e não do espaço
        Então, deve haver apenas um observador para cada tipo de agente. O observador observa o agente.
        Se eu tiver multiplas schedules - teria que montar um mecanismo de observação mais complexo.
        Uma possível solução é a schedule executar a ação do agente para cada espaço e 1 schedule -> N Espaços
        É necessário reestruturar a schedule para que ela funcione adequadamente.
    """

    def __init__(self, name, model, simulation, entity_class, agent_vars):
        self.name = name
        self.model = model
        self.simulation = simulation
        self.schedule = model.schedule
        self.observable_entity = entity_class
        self.agent_observables = {}
        self.agent_observation = {}
        self.observables_keys = {}
        self.observation_keys = {}
        self.obs_no = 0
        self.add_observables_keys()
        self.observation = None
        self.agent_vars = agent_vars
        self.define_observable_vars()
        self.create_observables()

    def define_observable_entity(self, entity_class):
        if entity_class not in self.model.dir():
            raise ValueError('{entity_class} not defined in the current scope')
        self.observable_entity = entity_class

    def add_observables_keys(self):
        self.observables_keys = {'model': [self.model.name],
                                 'simulation': [self.simulation.name],
                                 'scenario': [self.schedule.scenario_name],
                                 'run': [0],
                                 'step': [0],
                                 'time': [dt.datetime.now().isoformat(timespec='minutes')],
                                 'agent_name': [' ']}

    def update_observation_keys(self):
        self.observation_keys['model'] = self.model.name
        self.observation_keys['simulation'] = self.simulation.name
        self.observation_keys['scenario'] = self.schedule.scenario_name
        self.observation_keys['run'] = self.schedule.run_nr
        self.observation_keys['step'] = self.step
        self.observation_keys['time'] = dt.datetime.now().isoformat(timespec='minutes')

    def define_observable_vars(self):
        if self.observable_entity is not None:
            for var in self.agent_vars:
                self.agent_observables[var] = [0]
                self.agent_observation[var] = " "
        else:
            raise ValueError('{observable_entity} not defined')

    def basic_observation(self):
        self.observation = None
        agents_to_observe = self.model.agents_of_type(self.observable_entity)
        self.update_observation_keys()
        for agent_name, agent in agents_to_observe.items():
            self.observation_keys['agent_name'] = agent_name
            for agent_var_name in self.agent_observables.keys():
                self.agent_observation[agent_var_name] = getattr(agent, agent_var_name)
            self.observation = {**self.observation_keys, **self.agent_observation}
            self.append_observation()

    def create_observables(self):
        self.observables = {**self.observables_keys, **self.agent_observables}

    def append_observation(self):
        for var, value in self.observables.items():
            value.append(self.observation[var])

    def create_dataframe(self):
        self.observations = pd.DataFrame(self.observables)

    def save_dataframe(self, df_name):
        self.filename = 'runs/' + df_name
        self.observations.to_csv(self.filename, index_label='index_no')

    def observe(self, step):
        """ Implemented by subclass"""
        self.step = step
        self.basic_observation()


class ObserverCreator(object):
    """ Observer Generator - Observer Implemented Subclass must be used"""
    def __init__(self, model, simulation, observer_def):
        self.model = model
        self.simulation = simulation
        self.observers = {}
        for observer in observer_def:
            self.observer_type = observer['observer_type']
            self.observer_name = observer['observer_name']
            self.observer_agent = observer['observer_agent']
            self.observable_vars = observer['observable_vars']

            self.observer_model = self.model
            self.observer_simulation = self.simulation
            try:
                self.observer_class = eval(self.observer_type)
            except NameError:
                print("class ", self.observer_type, " is not defined")
            self.observer_Factory = ObserverProvider(self.observer_class)
            self.observer_Factory.add_args(self.observer_name,
                                           self.observer_model,
                                           self.observer_simulation,
                                           self.observer_agent,
                                           self.observable_vars)
            try:
                self.new_observer = self.observer_Factory()
                self.observers[self.observer_name] = self.new_observer
            except errors.Error as exception:
                print(exception)
                # <class '__main__.observer_Factory'>
                # does not know <'__main__.self.observer_name'>


class ObserverProvider(providers.Factory):
    """ Observer Provider Class"""
    provided_type = Observer
