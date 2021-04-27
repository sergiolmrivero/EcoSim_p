import os
import json
import redis
from abc import ABCMeta
from typing import Dict, List, Tuple
import re


class Database(metaclass=ABCMeta):    

    """
    Colections of methods to initializate and
    access Redis in memory Database
    """
    r = redis.Redis(host='localhost', port=6379, db=0)

    @staticmethod
    def initialize() -> None:
        print(os.getcwd())
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
        Database.r.set("models", json.dumps(list_models))

        ##############
        # Model Item #      
        ##############

        #################
        # -> 01: Agents #
        #################
        
        di_agents = {}

        for path_example_or_model in [path_examples, path_models]:
            print(30 * '-')

            li_models = list(filter(
                lambda file: '__' not in file and file[0] != '.', 
                os.listdir(path_example_or_model)))            

            li_path_models = list(map(
                lambda model: os.path.join(path_example_or_model, model), 
                li_models))            

            li_path_agents = list(map(
                lambda path: os.path.join(path, 'agents'), 
                li_path_models))            

            li_path_agent_files = list(map(
                lambda path: os.path.join(path, 'agents.py'), 
                li_path_agents))

            for path_agent_file in li_path_agent_files:

                with open(path_agent_file, 'r') as f:                   

                    model_name = path_agent_file.split(os.sep)[-3]

                    li_class_lines = list(filter(
                        lambda line: 'class' in line and line[0] not in ['#', '"'], 
                        [_.replace('\n', '').strip() for _ in f.readlines()]))

                    pattern = re.compile(r'class (\w+)\((\w+)\)')                                        

                    classes_and_subclasses: List[Tuple[str, str]] = list(map(
                        lambda line: pattern.search(line).groups(), 
                        li_class_lines))

                    agent_abstract_classes: List[str] = [abst for _, abst in classes_and_subclasses]

                    agent_concrete_classes: List[str] = [clse for clse, _ in classes_and_subclasses if clse not in agent_abstract_classes]

                    di_agents[model_name] = agent_concrete_classes

        Database.r.set("agents", json.dumps(di_agents))

        #################
        # -> 02: Spaces #
        #################

    @staticmethod
    def get(key: str) -> Dict:      
        return {key: json.loads(Database.r.get(key))}
