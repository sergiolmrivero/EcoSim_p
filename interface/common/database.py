import os
import json
import redis
from abc import ABCMeta
from typing import Dict


class Database(metaclass=ABCMeta):
	"""
	Colections of methods to initializate and
	access Redis in memory Database
	"""
	r = redis.Redis(host='localhost', port=6379, db=0)

	@staticmethod
	def initialize() -> None:
		"""
		Get examples from the examples directory
		Get models from the models directory
		"""     
		example_and_model_files: List[str] = []        
		path_examples = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'examples')     
		path_models: str = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'models')
		example_and_model_files.extend(os.listdir(path_examples))
		example_and_model_files.extend(os.listdir(path_models))
		list_models = sorted(list(set(filter(
			lambda file: '__' not in file, example_and_model_files))))
		Database.r.set("models", json.dumps(list_models))


	@staticmethod
	def get(key: str) -> Dict:		
		return {key: json.loads(Database.r.get(key))}
