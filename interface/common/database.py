import os
from typing import List, Dict


class Database:
    """
    Access data (parameters) from implicit database
    Retrive data in a format to send to the interface (webpage)
    """    
       
    @staticmethod
    def get_models() -> Dict:
        """
        Get examples from the examples directory
        """     
        examples_files: List[str] = []        
        path_examples = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'examples')     
        examples_files.extend(os.listdir(path_examples))
        
        return {
            "models": list(set(filter(lambda file: '__' not in file, examples_files)))
        }        
