# -*- coding: utf-8 -*-
"""
Python Economic ABM 

"""
import datetime


from .simulation import Simulation
from .model import Model

from .basicSpaces import Space
from .spaceCreation import SpaceCreator
from .spaceCreation import SpaceProvider

from .basicAgents import Agent
from .agentCreation import AgentPopulationCreator
from .agentCreation import AgentProvider

from .basicObservers import Observer
from .observerCreation import ObserverCreator
from .observerCreation import ObserverProvider

from .basicScenarios import Scenario
from .scenarioCreation import ScenarioCreator
from .scenarioCreation import ScenarioProvider

from .basicSchedule import Schedule
from .scheduleCreation import ScheduleCreator
from .scheduleCreation import ScheduleProvider

__all__ = [ "Simulation", "Model",
            "Space", "SpaceCreator", "SpaceProvider",
            "Agent", "AgentPopulationCreator", "AgentProvider",
            "Observer", "ObserverCreator", "ObserverProvider",
            "Scenario", "ScenarioCreator", "ScenarioProvider",
            "Schedule", "ScheduleCreator", "ScheduleProvider"]


__title__ = 'kernel'
__version__ = '0.0.0.Alpha'
__license__ = 'gnu'
__copyright__ = 'Copyright %s Ecos_p Team' % datetime.date.today().year
