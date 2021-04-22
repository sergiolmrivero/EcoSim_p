import os
from typing import List, Dict


class Database:
    """
    Access data (parameters) from implicit database
    Retrive data in a format to send to the interface (webpage)
    """    
       
    @staticmethod
    def get_models() -> Dict[str]:
        """
        Get examples from the examples directory
        Get models from the examples directory
        -> return: Dict[examples and models]
        """     
        example_and_model_files: List[str] = []        
        path_examples: str = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'examples')
        path_models: str = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'models')
        example_and_model_files.extend(os.listdir(path_examples))
        example_and_model_files.extend(os.listdir(path_models))
        
        return {
            "models": list(set(filter(lambda file: '__' not in file, example_and_model_files)))
        }        
