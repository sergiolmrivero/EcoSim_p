import os
from flask import jsonify # generate json
import json
import sys


# Orientação a objetos
# https://professormarcolan.com.br/como-utilizar-a-heranca-em-python/
# https://pt.wikibooks.org/wiki/Python/Conceitos_b%C3%A1sicos/Heran%C3%A7a_e_polimorfismo

"""
Access data (parameters) from implicit database
"""
class ParameterProvider():
	def __init__(self):
		self.models = {'models': []}
		self.spaces = {'spaces': []}
		self.agents = {'agents': []}
		self.scenarios = {'scenarios': []}
		
	def get_models(self):		

		path_examples = os.path.join(os.sep.join(os.getcwd().split(os.sep)[:-1]), 'examples')
		example_files = os.listdir(path_examples)

		for example in example_files:
		    if not '__' in example:
		        self.models['models'].append(example)

		return self.models

	def get_spaces(self, model_name):
		 #TODO: get the model from request the submited form by POST HTTP method
	    # model = request.form["model"]	       
	    print("modelo escolhido: {} -> {}".format(model_name, type(model_name)))
	

	    #TODO: get __ini__.py (spaces)
	    path_to_spaces_init_file = os.path.join(
	    	os.sep.join(os.getcwd().split(sep=os.sep)[:-1]), 
	    	'examples', model_name, 'spaces', '__init__.py')

	    #TODO: get spaces from __ini__.py (spaces)
	    # from .game import EFBGame
	    with open(path_to_spaces_init_file, "r") as f:
	        lines = f.readlines()
	        for line in lines:
	            if "import" in line:
	                line_elements = line.split(sep=" ")
	                # print(line_elements)
	                is_import = False
	                for elem in line_elements:                
	                    if is_import:
	                        space = elem.replace('\n', '')
	                        # print(space)
	                        self.spaces['spaces'].append(space)
	                    if elem == "import":
	                        is_import = True
	                        
	    return self.spaces

	def get_agents(self, model_name):
		#TODO: get __init__.py (agents)
	    path_to_agents_init_file = os.path.join(os.sep.join(os.getcwd().split(sep=os.sep)[:-1]), 'examples', model_name, 'agents', '__init__.py')

	    #TODO: get agents from __init__.py (agents)
	    # __all__ = ["Player", "RandomPlayer"]

	    with open(path_to_agents_init_file, "r") as f:
	        lines = f.readlines()
	        for line in lines:
	            if "__all__ = " in line:
	                colchet_begin = line.index('[') + 1
	                colchet_end = line.index(']')

	                agents = [elem.replace(" ", "")[1:-1] for elem in line[colchet_begin:colchet_end].split(sep=',')]
	                # print(line_elements, line_elements.__len__())       
	                for agent in agents:
	                    self.agents['agents'].append(agent)

	    return self.agents

	#TODO
	def get_scenarios(self, model_name):
		pass


"""
Storage the model parameters
received from parametrization page

Storage the simulation parameters
received from simulation page
"""
class SimulationParameters():	
	def __init__(self):
		self.model_name = ''
		self.model_parameters = {}
		self.simulation_parameters = {}	
		self.path_to_export_json = ''


"""
Receive both
Model and Simulation parameters
from Parameters class and
Generate JSON
"""
class ParameterResolution(SimulationParameters):	
	def __init__(self):
		super().__init__()
		self.dictionary_parameters = {} # will be parse to JSON
		self.path_json_file = ''

	# TODO
	def generate_dictionary_parameters(self):
		pass
		
	#TODO
	def export_json_parameters_file(self, json_file_name = None):
		if json_file_name == None:
			json_file_name = self.model_name + '.json'
		self.path_json_file = self.path_to_export_json + json_file_name
		with open(self.path_json_file, 'w') as f:

			return json.dump(dictionary_parameters, f)
	


class ExecuteSimulation(ParameterResolution):
	#TODO
	def __init__(self):
		super().__init__(self, dictionary_parameters, path_json_file)		
		self.path_simulator = ''

	def exec_simulation(self):

		execfile(path_simulator)
