import os
import sys
from abc import ABCMeta, abstractmethod
from typing import Dict

class ParameterProvider():
	"""
	Access data (parameters) from implicit database
	Retrive data in a format to send to the interface (webpage)
	"""

	def __init__(self) -> None:
		"""
		__init__ method is like the constructor method from the ParameterProvider object

		The models, spaces (future), agents (future), action_sets (future) and scenarios (future) are not passed as parameters
		for the constructor because they will be obtained along the user interaction
		"""

		self._models: dict = {'models': []}
		

	def get_models(self):
		"""
		Get models from the examples directory
		"""		

		path_examples = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'examples')
		example_files = os.listdir(path_examples)

		for example in example_files:
			if '__' not in example:

				# TO check if the model had already been storage in self.models
				# Avoid storage again in case of refresh the homepage
				# It may be did using a set in opposite to dictionary
				# But dictionary is the best format for the REST API
				if example not in self._models['models']:
					self._models['models'].append(example)

				else:
					print(f'example {example} had already been stored')

		return self._models

		@property
		def models(self) -> dict:
			return self._models
		
		@models.setter
		def models(self, value:dict) -> None:
			self._models = value
		
class ExecuteSimulationFromJson():
	"""
	Execute Simulation from JSON file by one of the two ways:

	1. Take a pre-existing JSON file as parameters entry to execute the simulation (OK)
	2. Generate the JSON file and use it as parameters entry to execute the simulation
	
	"""

	def __init__(self, path_to_app_server:str) -> None:
		"""
		__init__ method is like the constructor method from the ExecuteSimulationFromJson object
		
		"""
		self._PATH_TO_APP_SERVER: str = path_to_app_server
		self._model_name: str = ''
		self._path_to_model: str = ''
		self._script_shell_file_name: str = ''
		
		
	def exec_simulation(self, model_name: str) -> None:
		"""
		Execute the simulation by the JSON
		Execute from a script shell placed ate selected model directory
		"""

		self._model_name = model_name
		print(os.sep.join(self._PATH_TO_APP_SERVER.split(sep=os.sep)[:-1]))
		self._path_to_model = os.path.join(os.sep.join(self._PATH_TO_APP_SERVER.split(sep=os.sep)[:-1]), 'examples', self._model_name)


		# STEP 1: Change to the example directory	
		os.chdir(self._path_to_model)

		# STEP 2: Get the .sh name files at the model directory
		li_sh_files = [file for file in os.listdir() if '.sh' in file]
		
		# STEP 3: Get the .sh file
		if len(li_sh_files) == 1:
						
			self._script_shell_file_name = li_sh_files[0]			

		else:
			sys.exit('There is more then one .sh script in the model directory\nPlease, let just one of them and exclude the other(s)')
					

		# STEP 4: Execute the .sh file
		os.system(f'./{self._script_shell_file_name}')		

		# STEP 5: Set the pwd to the server PATH
		os.system('cd ' + self._PATH_TO_APP_SERVER)
		os.chdir(self._PATH_TO_APP_SERVER)


	@property
	def PATH_TO_APP_SERVER(self) -> str:
		return self._PATH_TO_APP_SERVER

	@PATH_TO_APP_SERVER.setter
	def PATH_TO_APP_SERVER(self, value:str) -> None:
		if self._PATH_TO_APP_SERVER == '':
			sys.exit("Error: PATH_TO_APP_SERVER cannot change along the server execution")
		self._PATH_TO_APP_SERVER = value

	@property
	def model_name(self) -> str:
		return self._model_name

	@model_name.setter
	def model_name(self, value:str) -> None:
		self._model_name = value
	
	@property
	def path_to_model(self) -> str:
		return self._path_to_model

	@path_to_model.setter
	def path_to_model(self, value:str) -> None:
		self._path_to_model = value
	
	@property
	def script_shell_file_name(self) -> str:
		return self._script_shell_file_name

	@script_shell_file_name.setter
	def script_shell_file_name(self, value) -> None:
		self._script_shell_file_name = value

class Json(metaclass=ABCMeta):
	"""
	Json operations
	1. save parameters
	"""
	__path_to_model: str = None
	__script_shell_file_name: str = None	

	# TODO
	@abstractmethod
	def save_parameters(parameters: str, model_name: str) -> None:
		"""
		Save json parameters retrieved by the user in the model path
		"""
		print('saving')
		abs_path_to_storage_json_parameters = os.path.join(__path_to_model, get_json_name_of_the_model())
		with open(__path_to_model, 'w') as f:
			f.write(parameters)

	@abstractmethod
	def get_json_name_of_the_model(model_name) -> str:
		"""
		Return: str -> the json name defined by the .sh file to execute the selected model
		"""
				

		# STEP 1: Get the .sh name files at the model directory
		li_sh_files = [file for file in os.listdir(__path_to_model) if '.sh' in file]
		
		# STEP 2: Get the .sh file
		if len(li_sh_files) == 1:
						
			__script_shell_file_name = li_sh_files[0]			

		else:
			sys.exit('There is more then one .sh script in the model directory\nPlease, let just one of them and exclude the other(s)')
					

		# STEP 4: Read lines of the scrip shell file
		abs_path_to_script_shell = os.path.join(__path_to_model, __script_shell_file_name)

		with open(abs_path_to_script_shell) as f:
			for line in f.readlines():
				if '.json' in line:
					print(line)
					l = line.split(sep=' ')
					for term in line:
						if '.json' in term:
							print(term)
							return 'test_' + term

	@abstractmethod
	def set_path_to_model(model_name: str, path_to_app_server: str) -> None:
		__path_to_model = os.path.join(os.sep.join(path_to_app_server.split(sep=os.sep)[:-1]), 'examples', model_name)
