#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Observer

*SLMR
"""

import dependency_injector.providers as providers
import dependency_injector.errors as errors


class Observer(object):
    """ Schedule Class """

    def __init__(self, name, model, simulation):
        self.name = name
        self.model = model
        self.space = simulation
        self.scenario_name = " "

    def observe(self):
        """ Implemented by subclass"""
        pass

# Definir a EventSchedule
# Eventualmente, implementar o Agente para diferentes tipos de schd
# Montar um modelo macroeconômico básico (Usando Hilder)
# Incluir um dataframe para observação e montar estrutura de observação


class EventObserver(Observer):
    """ An Event Schedule """
    def __init__(self, name, model, simulation):
        """ PoolSchedule initialization """
        super().__init__(name, model, simulation)
        self.events = dict()

    def observe(self, an_event):
        self.events[an_event.event_id] = an_event


class PoolObserver(Observer):
    """ A pool Observer for test"""
    def __init__(self, name, model, simulation):
        """ PoolObserver initialization """
        super().__init__(name, model, simulation)
        self.run_nr = " "

    def init_pool_observation
    (self, scenario_name, run_nr):
        self.run_nr = run_nr
        self.scenario_name = scenario_name


class ModelPoolObserver(PoolObserver):
    def __init__(self, name, model, simulation):
        """ PoolObserver initialization """
        super().__init__(name, model, simulation)
        self.run_nr = None
        self.step = None

    def observe(self):
        pass


class ObserverCreator(object):
    """ Observer Generator - Observer Implemented Subclass must be used"""
    def __init__(self, model, simulation, observer_def):
        self.model = model
        self.simulation = simulation
        for observer in observer_def:
            self.observer_type = observer['observer_type']
            self.observer_name = observer['observer_name']
            self.observer_model = self.model
            self.observer_simulation = self.simulation
            try:
                self.observer_class = eval(self.observer_type)
            except NameError:
                print("class ", self.observer_type, " is not defined")
            self.observer_Factory = ObserverProvider(self.observer_class)
            self.observer_Factory.add_args(self.observer_name,
                                           self.observer_model,
                                           self.observer_simulation)
            try:
                self.new_observer = self.observer_Factory()
            except errors.Error as exception:
                print(exception)
                # <class '__main__.observer_Factory'>
                # does not know <'__main__.self.observer_name'>
            self.provided_observer = self.new_observer


class ObserverProvider(providers.Factory):
    """ Observer Provider Class"""
    provided_type = Observer
