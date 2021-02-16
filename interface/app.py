from flask import Flask, request, render_template
from flask_restful import Resource, Api
import os

from modules.interface import ParameterProvider, ExecuteSimulationFromJson

"""
HTTP Status                                                   
200 - Ok
201 - Created
404 - Error
"""

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
api = Api(app)

parameter_provider = ParameterProvider()
executeSimulationFromJson = ExecuteSimulationFromJson(path_to_app_server=os.getcwd())

@app.route('/', methods=['GET'])
def parametrization():
    """
    Route to render the parametrization page
    """

    return render_template('/parametrization/parametrization.html')


@app.route('/simulation', methods=['GET', 'POST'])
def simulation():
    """    
    Receive the model_name from a POST Request from the homepage    
    Execute the simulation (of the choosen model) itself
    Render the simulation web page
    """

    model_name = request.form["model"]    
    executeSimulationFromJson.exec_simulation(model_name)

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
    