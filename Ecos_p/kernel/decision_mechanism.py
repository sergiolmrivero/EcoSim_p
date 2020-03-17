#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Definition of the class Decision_Mechanism

*SLMR
"""


class Decision_Mechanism(object):
    """ The agent memory """

    def __init__(self, an_agent):
        """DM initialization"""
        self.owner = an_agent

    def set_rules(self, agent_role, space):
        pass

    def set_actions(self, agent_role, space):
        pass

    def decides(self):
        """ Uses sensors in space-time to capture env variables"""
        return 0   # ## Must be implemented
