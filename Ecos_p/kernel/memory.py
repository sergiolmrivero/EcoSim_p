#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Memory

*SLMR
"""


class Memory(object):
    """ The agent memory """

    def __init__(self, an_agent):
        """Memory initialization"""
        self.agent = an_agent
        self.state_variables = {}
        self.events = {}

    def initialize_state_variables(self, state_variables):
        # ou a classe Data ou a Classe Memory vai ter este método.
        """ Initalize state variables - This method will need to use JSON"""
        for variable in state_variables:
            self.state_variables[variable.name] = variable.value

    def initialize_state_events(self, events):
        """ Initalize state variables - This method will need to use JSON"""
        for event_id in events:
            self.events[event_id] = events.event

    def set_data(self, agent_role, space):
        # Precisa utilizar uma definicao feita com json
        pass

    def perceives(self):
        """ Uses sensors in space-time to capture env variables"""
        return 0

    def update(self, event):
        self.events[event.event_id] = event

    def update_event(self, event):
        self.events[event.event_id] = event

    def update_state_variable(self, state_variable):
        self.state_variables[state_variable.name] = state_variable.value
