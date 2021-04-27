from flask_restful import Resource

from models.agent import Agent


class AgentList(Resource):
    """
    RESTful API for consulting/list the agents of a model that can be simulated
    """

    def get(self):
        """
        Get Agents organized by models
        """

        return Agent.json(), 200
