from flask import Flask, request, render_template
from flask_restful import Resource, Api
import os

from modules.interface import ParameterProvider, ExecuteSimulationFromJson, Json

"""
HTTP Status                                                   
200 - Ok
201 - Created
404 - Error
"""

"""
Global Variables
"""
MODEL: str = None                   # storage the model name to be simulated. The user entry with this by the interface
PATH_TO_MODEL: str = None           # storage the path to the model to be simulated

"""
Server Settings
"""
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
api = Api(app)


"""
objects
"""
parameter_provider = ParameterProvider()
executeSimulationFromJson = ExecuteSimulationFromJson(path_to_app_server=os.getcwd())

@app.route('/', methods=['GET'])
def homepage():
    """
    Route to render the homepage
    """

    return render_template('/homepage.html')

@app.route('/parametrization', methods=['GET', 'POST'])
def parametrization():
    global MODEL
    global PATH_TO_MODEL    
    """
    1.Recieve the model to be simulated by the homepage
    2.Open an text area to the user
        setting up the json file
        which defines the
        simulation parameters
    3.Calculate the path to model
    4.List the files in the path to model
    """

    MODEL = request.form["model"]
    PATH_TO_MODEL = Json.calc_path_to_model(model_name=MODEL, path_to_app_server=os.getcwd())
    print('\n\nPATH TO MODEL: ', PATH_TO_MODEL)

    return render_template('/parametrization.html')


@app.route('/simulation', methods=['GET', 'POST'])
def simulation():
    global PATH_TO_MODEL
    """    
    Receive the model_name from a POST Request from the homepage    
    Execute the simulation (of the choosen model) itself
    Render the simulation web page
    """
    
    parameters: str =  request.form["textarea-parameters"]
    Json.save_parameters(parameters=parameters, path_to_model=PATH_TO_MODEL)
    executeSimulationFromJson.exec_simulation(path_to_model=PATH_TO_MODEL)

    return render_template('/simulation.html')


class ModelList(Resource):
    """
    RESTful API for consulting/list the models that can be simulated
    """

    def get(self):                
        """
        GET the models which the user will choose to simulate
        """

        return parameter_provider.get_models(), 200        

api.add_resource(ModelList, '/models')

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)  # important to mention debug=True
    