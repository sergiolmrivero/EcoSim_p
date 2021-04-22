from flask_restful import Resource

from common.database import Database

class ModelList(Resource):
    """
    RESTful API for consulting/list the models that can be simulated
    """

    def get(self):                
        """
        GET the models which the user will choose to simulate
        """

        return Database.get_models(), 200
