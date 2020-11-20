# -*- coding: utf-8 -*-
"""
Definition of the class Memory
"""


class Memory(object):
    """ The agent memory """

    def __init__(self, an_agent):
        """ Memory initialization """
        self.agent = an_agent
        self.state_variables = {}
        self.events = {}

    def initialize_state_variables(self, state_variables):
        """ Initialize state variables"""
        for variable in state_variables:
            self.state_variables[variable.name] = variable.value

    def initialize_state_events(self, events):
        """ Initialize state variables """
        for event_id in events:
            self.events[event_id] = events.event

    def set_data(self, agent_role, space):
        """ Set data used in agent memory"""
        pass

    def perceives(self):
        """ Uses sensors in space-time to capture env variables """
        return 0

    def update_event(self, event):
        """ Update agent events """
        self.events[event.event_id] = event

    def update_state_variable(self, state_variable):
        """ Update agent state variables """
        self.state_variables[state_variable.name] = state_variable.value

# TODO: Check the necessity of this class
