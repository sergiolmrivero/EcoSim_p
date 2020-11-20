# -*- coding: utf-8 -*-
"""
Definition of the class Decision_Mechanism
"""

class Decision_Mechanism(object):
    """ The agent Decision Mechanism """

    def __init__(self, an_agent):
        """ DM initialization """
        self.owner = an_agent

    def set_rules(self, agent_role, space):
        """ Set rules for the agent dm """
        pass

    def set_actions(self, agent_role, space):
        """ Set agent actions """
        pass

    def decides(self):
        """ Uses sensors in space-time to capture env variables """
        return 0

# TODO: Revise this class to integrante in the version 0.0.1
