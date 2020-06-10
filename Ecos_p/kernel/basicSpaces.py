# -*- coding: utf-8 -*-
"""
The space class and the associated classes
"""
from collections import OrderedDict


class Space(object):
    """ The space class """
    def __init__(self, model, name,
                 actions_set_file,
                 action_class):
        """ Initialize Space Class """

        self.model = model
        self.name = name
        self.agents = OrderedDict()

    def enter(self, agent_name, agent):
        """ An agent enter the a space object """
        if agent_name not in self.agents:
            self.agents[agent_name] = agent

    def exit(self, agent_name):
        """ An agent exits a space object """
        if agent_name in self.agents:
            del self.agents[agent_name]

    def update(self):
        """
        A Space updates its values and execute methods
        This method is impmented by space subclass
        """
        pass
