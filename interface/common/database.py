import os
# import json
# import redis
from typing import Dict, List, Any


class Database:    
    """
    Colections of methods to initializate and
    access in memory Database
    """

    # Redis
    # r = redis.Redis(host='localhost', port=6379, db=0)
    parameters: Dict = {}
    
    @staticmethod
    def initialize() -> None:        
        """
        Initialize database
        Get examples from the examples directory
        Get models from the models directory
        """

        ##############
        # Model List #
        ##############

        example_and_model_files: List[str] = []        
        path_examples = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'examples')     
        path_models: str = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'models')
        example_and_model_files.extend(os.listdir(path_examples))
        example_and_model_files.extend(os.listdir(path_models))
        list_models = sorted(list(set(filter(
            lambda file: '__' not in file, example_and_model_files))))

        # Redis
        # Database.r.set("models", json.dumps(list_models))
        Database.parameters['models'] = list_models

    @staticmethod
    def get(key: str) -> Dict:      
        # Redis
        # return {key: json.loads(Database.r.get(key))}
        return {key: Database.parameters[key]}

    @staticmethod
    def set(key: str, value: Any) -> None:
        Database.parameters[key] = value
        return None
