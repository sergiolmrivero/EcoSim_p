#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class ScheduleCreator

*SLMR
REMEMBER TO USE DEPENDENCE INJECTION IN THE CODE.
http://python-dependency-injector.ets-labs.org/index.html

"""

import dependency_injector.providers as providers
import dependency_injector.errors as errors
import basicSchedule as schd


class ScheduleCreator(object):
    """ Schedule Generator - Schedule Implemented Subclass must be used"""
    def __init__(self, model, schedule_def):
        self.model = model
        for schedule in schedule_def:
            self.schedule_type = schedule['schedule_type']
            self.schedule_name = schedule['schedule_name']
            self.schedule_model = self.model
            try:
                a_schedule = "schd" + "." + self.schedule_type
                self.schedule_class = eval(a_schedule)
            except NameError:
                print("class ", self.schedule_type, " is not defined")
            self.schedule_Factory = ScheduleProvider(self.schedule_class)
            self.schedule_Factory.add_args(self.schedule_name,
                                           self.schedule_model)
            try:
                self.new_schedule = self.schedule_Factory()
            except errors.Error as exception:
                print(exception)
                # <class '__main__.schedule_Factory'>
                # does not know <'__main__.self.schedule_name'>
            self.provided_schedule = self.new_schedule


class ScheduleProvider(providers.Factory):
    """ Agent Provider Class"""
    provided_type = schd.Schedule
