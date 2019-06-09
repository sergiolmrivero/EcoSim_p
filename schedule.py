#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of the class Schedule

*SLMR
REMEMBER TO USE DEPENDENCE INJECTION IN THE CODE.
http://python-dependency-injector.ets-labs.org/index.html

"""

import dependency_injector.providers as providers
import dependency_injector.errors as errors


class Schedule(object):
    """ Schedule Class """

    def __init__(self, name, model, space):
        self.name = name
        self.model = model
        self.space = space
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
    def __init__(self, name, model, space):
        """ PoolSchedule initialization """
        super().__init__(name, model, space)
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
    def __init__(self, name, model, space):
        """ PoolSchedule initialization """
        super().__init__(name, model, space)
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
                for agent_name, agent in self.model.simulation.agents.items():
                    agent.step(this_step)
                for observer_name, observer in self.model.simulation.agent_observers.items():
                    observer.observe()
        else:
            raise Exception(step_unit,
                            "is not valid as step unity")


class ScheduleCreator(object):
    """ Schedule Generator - Schedule Implemented Subclass must be used"""
    def __init__(self, model, space, schedule_def):
        self.model = model
        self.space = space
        for schedule in schedule_def:
            self.schedule_type = schedule['schedule_type']
            self.schedule_name = schedule['schedule_name']
            self.schedule_model = self.model
            self.schedule_space = self.space
            try:
                self.schedule_class = eval(self.schedule_type)
            except NameError:
                print("class ", self.schedule_type, " is not defined")
            self.schedule_Factory = ScheduleProvider(self.schedule_class)
            self.schedule_Factory.add_args(self.schedule_name,
                                           self.schedule_model,
                                           self.schedule_space)
            try:
                self.new_schedule = self.schedule_Factory()
            except errors.Error as exception:
                print(exception)
                # <class '__main__.schedule_Factory'>
                # does not know <'__main__.self.schedule_name'>
            self.provided_schedule = self.new_schedule


class ScheduleProvider(providers.Factory):
    """ Agent Provider Class"""
    provided_type = Schedule
