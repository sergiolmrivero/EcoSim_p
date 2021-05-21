##############
# Controller #
##############

import os
from flask import Flask
from flask_restful import Api

from common.database import Database
from resources.model import ModelList
from views.homepage import homepage_blueprint
from views.simulation import simulation_blueprint
from views.result import result_blueprint

"""
HTTP Status
200 - Ok
201 - Created
404 - Error
204 - No Content
"""

#####################
# Flask basic Setup #
#####################
path_pages = os.path.join(os.getcwd(), 'pages')
app = Flask(__name__, template_folder=path_pages, static_folder=path_pages)

app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app

app.secret_key = os.urandom(64)

#############
# Endpoints #
#  (Views)  #
#############

app.register_blueprint(homepage_blueprint, url_prefix="/")
app.register_blueprint(simulation_blueprint, url_prefix="/simulation")
app.register_blueprint(result_blueprint, url_prefix="/result")

#############
# Resources #
# (Models)  #
#############

api = Api(app)
api.add_resource(ModelList, '/models')

##################
# Initialization #
##################

@app.before_first_request
def init_db():
    Database.initialize()

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)  # important to mention debug=True
