import os
from typing import List, Dict
from dataclasses import dataclass
from models.abstract_data_model import AbstractDataModel


@dataclass
class Model(AbstractDataModel):
    """
    Access data (parameters) from implicit database
    Retrive data in a format to send to the interface (webpage)
    """    
    
    def all() -> Dict:
        """
        Get examples from the examples directory
        Get models from the models directory
        """     
        example_and_model_files: List[str] = []        
        path_examples = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'examples')     
        path_models: str = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'models')
        example_and_model_files.extend(os.listdir(path_examples))
        example_and_model_files.extend(os.listdir(path_models))
        
        return {
            "models": sorted(list(set(filter(lambda file: '__' not in file, example_and_model_files))))
        }        
