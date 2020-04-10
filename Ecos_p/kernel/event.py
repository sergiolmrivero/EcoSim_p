# -*- coding: utf-8 -*-
"""
Definition of the class Event
"""


class Event(object):
    """ The events handled by the agent and the space"""

    def __init__(self, an_agent, a_space, an_action):
        """ Initialize an event object """
        self.agent = an_agent
        self.space = a_space
        self.action = an_action
        self.valid_status = ('new', 'active', 'executed', 'completed')
        self.status = 'new'
        self.event_id_nr = 0
        self.generate_event_id()

    def generate_event_id(self):
        """ Generates an unique ID for and event """
        self.event_id_nr = self.event_id_nr + 1
        ag_id_str = str(self.id)
        spc_name_str = str(self.space.space_name)
        self.event_id = ag_id_str + spc_name_str + str(self.event_id_nr)

    def set_status(self, new_status):
        """ Set status for an event """
        if new_status not in self.valid_status:
            raise ValueError('{new_status} is not a correct status!')
        self.status = new_status

# TODO: Revise the implementation of events - Actually events execution is not implemented.