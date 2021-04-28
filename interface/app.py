##############
# Controller #
##############

import os
from flask import Flask
from flask_restful import Api

from common.database import Database
from resources.model import ModelList
from resources.agent import AgentList
from views.parametrization import parametrization_blueprint
from views.show_results import show_results_blueprint
from views.simulation import simulation_blueprint

"""
HTTP Status
200 - Ok
201 - Created
404 - Error
"""

#####################
# Flask basic Setup #
#####################

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = os.urandom(64)

#############
# Endpoints #
#  (Views)  #
#############

app.register_blueprint(parametrization_blueprint, url_prefix="/")
app.register_blueprint(simulation_blueprint, url_prefix="/simulation")
app.register_blueprint(show_results_blueprint, url_prefix="/show_results")

#############
# Resources #
# (Models)  #
#############

api = Api(app)
api.add_resource(AgentList, '/agents')
api.add_resource(ModelList, '/models')

##################
# Initialization #
##################

@app.before_first_request
def init_db():
    Database.initialize()

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)  # important to mention debug=True
