#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of the class Event

*SLMR
"""


class Event(object):
    """ The events handled by the agent and the space"""

    def __init__(self, an_agent, a_space, an_action):
        self.agent = an_agent
        self.space = a_space
        self.action = an_action
        self.valid_status = ('new', 'active', 'executed', 'completed')
        self.status = 'new'
        self.event_id_nr = 0
        self.generate_event_id()

    def generate_event_id(self):
        self.event_id_nr = self.event_id_nr + 1
        ag_id_str = str(self.id)
        spc_name_str = str(self.space.space_name)
        self.event_id = ag_id_str + spc_name_str + str(self.event_id_nr)

    def set_status(self, new_status):
        if new_status not in self.valid_status:
            raise ValueError('{new_status} is not a correct status!')
        self.status = new_status
