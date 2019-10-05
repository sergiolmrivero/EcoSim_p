#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Schedule

*SLMR
REMEMBER TO USE DEPENDENCE INJECTION IN THE CODE.
http://python-dependency-injector.ets-labs.org/index.html

"""

class Schedule(object):
    """ Schedule Class """

    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.scenario_name = " "

    def execute(self, scenario_name,
                step_unit,
                step_interval,
                no_of_steps,
                run_nr):
        """ Interface for the execute method of schedule objects
            Implemented by subclass
        """
        raise NotImplementedError("Must subclass me")


# Definir a EventSchedule
# Eventualmente, implementar o Agente para diferentes tipos de schd
# Montar um modelo macroeconômico básico (Usando Hilder)


class EventSchedule(Schedule):
    """ An Event Schedule """
    def __init__(self, name, model):
        """ PoolSchedule initialization """
        super().__init__(name, model)
        self.events = dict()

    def collect_event(self, an_event):
        self.events[an_event.event_id] = an_event

    def execute(self, scenario_name,
                step_unit,
                step_interval,
                no_of_steps,
                run_nr):
        pass


class PoolSchedule(Schedule):
    """ A pool schedule for test"""
    def __init__(self, name, model):
        """ PoolSchedule initialization """
        super().__init__(name, model)
        self.run_nr = " "

    def execute(self, scenario_name,
                step_unit,
                step_interval,
                no_of_steps,
                run_nr):
        self.run_nr = run_nr
        self.scenario_name = scenario_name
        if step_unit == 'step':
            for this_step in range(0, no_of_steps, step_interval):
                for agent_name, agent in self.model.agents.items():
                    agent.step(this_step)
                for observer_name, observer in self.model.agent_observers.items():
                    observer.observe(this_step)
        else:
            raise Exception(step_unit,
                            "is not valid as step unity")