import os
from flask import Flask
from flask_restful import Api

from resources.model import ModelList

from views.parametrization import parametrization_blueprint
from views.show_results import show_results_blueprint

"""
HTTP Status                                       s            
200 - Ok
201 - Created
404 - Error
"""

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = os.urandom(64)

api = Api(app)

app.register_blueprint(parametrization_blueprint, url_prefix="/")
app.register_blueprint(show_results_blueprint, url_prefix="/show_results")

api.add_resource(ModelList, '/models')

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)  # important to mention debug=True
