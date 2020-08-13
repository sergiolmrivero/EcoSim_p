from flask import Flask, request, render_template, make_response, Response, jsonify, url_for
from flask_restful import Resource, Api, reqparse

from modules.interface import ParameterProvider, SimulationParameters, ParameterResolution

# https://stackoverflow.com/questions/32274392/flask-restful-render-template-cannot-work


#TODO: Futurelly, allow to execute simuladions from stored json files

"""
HTTP Status
200 - Ok
201 - Created
404 - Error
"""
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
api = Api(app)

"""
ParameterProvider() retrive data in a format to send to the interface (webpage)
Parameter() storage both model and simulation parameters
ParametersResolution () parse and write the parameters to a json file
"""
parameter_provider = ParameterProvider()
parameters = SimulationParameters()
parameters_resolution = None


"""
Routes for rendering pages
"""

@app.route('/', methods=['GET'])
def homepage():
    return render_template('/homepage.html')

@app.route('/parametrization', methods=['GET'])
def parametrization():
    return render_template('/parametrization.html')

@app.route('/simulation', methods=['GET'])
def simulation():
    parameters_resolution = ParameterResolution(parameters)
    return render_template('/simulation.html')

@app.route('/results', methods=['GET'])
def results():
    return render_template('/results.html')

"""
RESTful APIs
"""
class ModelList(Resource):
    def get(self):                
        # return parameter_provider.get_models(), 200
        return {'models': ['model A', 'model B']}, 200


class SpacelList(Resource):
    def get(self):
        return parameter_provider.get_spaces(model_name = parameters.model_name), 200
        # return {'spaces': ['space A', 'space B']}, 200


class AgentList(Resource):
    def get(self):
        return parameter_provider.get_agents(model_name = parameters.model_name), 200
        # return {'agents': ['agent A', 'agent B']}, 200

#TODO
class ScenarioList(Resource):
    def get(self):
        # return parameter_provider.get_scenarios(), 200
        return {'scenarios': ['scenario A', 'scenario B']}, 200


class ModelItem(Resource):
    def get(self, name):
        print(name)           
        model_name = parameters.model_name
        print(model_name)
        return {"name": model_name}, 200
        
    def post(self, name):

        # way 1
        """        
        model_name = request.get_json()["model"] # get the requisition at the body of the post request
        # print(request.get_json()["key_for_test_in_API"])
        parameters.model_name = model_name        
        return {"model": model_name}, 201
        """
        # way 2 (more simple)        
        parameters.model_name = name
        return {"name": name}, 201

#TODO
class ParameterList(Resource):
    def post(self):
        

        #TODO: API receive the file name to write the json parameters file
        """
        dictionary_of_parameters = request.get_json()["parameters"] # to be implemented
        json_file_name = request.get_json()["json_file_name"] # to be implemented
        """        

        return {'json_file_name': 'will be implemented (received from the user interface)', 'parameters': request.get_json()}


"""
Creating/Associating endpoint to each API
"""

# Lists - General
api.add_resource(ModelList, '/models')
api.add_resource(SpacelList, '/spaces')
api.add_resource(AgentList, '/agents')
api.add_resource(ScenarioList, '/scenarios')

# Items - Choosen Model
api.add_resource(ModelItem, '/model/<string:name>')

# Lists - Choosen Model
api.add_resource(ParameterList, '/parameters')

"""
Run Locally at http://127.0.0.1:5000/
"""

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)  # important to mention debug=True
