from dataclasses import dataclass

from models.abstract_data_model import AbstractDataModel
from common.database import Database


@dataclass
class Agent(AbstractDataModel):
    """
    Access data (parameters) from implicit database
    Retrive data in a format to send to the interface (webpage)
    """

    def json():
        """
        Get agents of a specific model the examples directory
        Get models from the models directory
        """

        return Database.get("agents")
