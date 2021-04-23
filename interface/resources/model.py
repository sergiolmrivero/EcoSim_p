from flask_restful import Resource

from models.model import Model

class ModelList(Resource):
    """
    RESTful API for consulting/list the models that can be simulated
    """

    def get(self):                
        """
        GET the models which the user will choose to simulate
        """

        return Model.all(), 200

