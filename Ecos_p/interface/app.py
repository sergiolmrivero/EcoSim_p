from flask import Flask, request, render_template, make_response, Response, jsonify
from flask_restful import Resource, Api, reqparse

from modules.interface import ParameterProvider

# https://stackoverflow.com/questions/32274392/flask-restful-render-template-cannot-work


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
api = Api(app)

"""
Class to retrive data in a format to send to the interface (webpage)
"""
parameter_provider = ParameterProvider()

"""
Routes
"""

@app.route('/')
def homepage():
    return render_template('/homepage.html')

@app.route('/parametrization')
def parametrization():
    return render_template('/parametrization.html')

@app.route('/simulation')
def simulation():
    return render_template('/simulation.html')

@app.route('/results')
def results():
    return render_template('/results.html')

"""
RESTful APIs
"""
class ModelList(Resource):    
    def get(self):                
        return parameter_provider.get_models()
        # return {'models': ['model A', 'model B']}


class SpacelList(Resource):
    def get(self):
        return parameter_provider.get_spaces()
        # return {'spaces': ['space A', 'space B']}


class AgentList(Resource):
    def get(self):
        return parameter_provider.get_agents()
        # return {'agents': ['agent A', 'agent B']}

#TODO
class ScenariosList(Resource):
    def get(self):
        return parameter_provider.get_scenarios()
        # return {'scenarios': ['scenario A', 'scenario B']}

"""
Creating/Associating endpoint to each API
"""
api.add_resource(ModelList, '/models')
api.add_resource(SpacelList, '/spaces')
api.add_resource(AgentList, '/agents')
api.add_resource(ScenariosList, '/scenarios')

"""
Run Locally at http://127.0.0.1:5000/
"""
if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)  # important to mention debug=True
